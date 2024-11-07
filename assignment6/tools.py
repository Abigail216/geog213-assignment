import pystac_client
import planetary_computer
import rioxarray as rx
import stackstac 
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

def main(api_url, collection, bbox, start_date, end_date, assets): 
    print("Main Running")
    """
    This function plots mean NDWI values vs. time. 

    Parameters: 
    --------------
    api_url: str
        The STAC API URL
    collection: str
        Collection ID to search in the STAC API
    bbox: tuple
        Bounding box coordinates in format (west, south, east, north)
    start_date: str
        Start date for searching scenes in YYYY-MM-DD format
    end_date: str
        End date for searching scenes in YYYY-MM-DD format
    assets: str
        List of red & green band names, 0 index is green and 1 index is NIR band

    Returns: 
    ---------------
    None, scatter plot of mean NDWI values over time. 
    """
    def search_api(api_url, collection, bbox, start_date, end_date):
        """
        This function searches an API based on date and area

        Parameters
        ------------
        
        api_url: str
            The STAC API URL
        collection: str
            Collection ID to search in the STAC API
        bbox: tuple
            Bounding box coordinates in format (west, south, east, north)
        start_date: str
            Start date for searching scenes in YYYY-MM-DD format
        end_date: str
            End date for searching scenes in YYYY-MM-DD format

        Returns
        ------------
        items: Collection of items matching the search criteria
        
        """
        print("Searching...")
        catalog = pystac_client.Client.open(
            url=api_url
        )
        search_results = catalog.search(
            collections=[collection],
            bbox=bbox,
            datetime=f"{start_date}/{end_date}"
        )
        items = search_results.item_collection()
        print(f"Found {len(items)} scenes")
        return items

    def create_stackstac(items, assets , bbox):
        """
        This function returns a xarray object using stackstac with the requested assets 
        stacked and clipped to the bbox

        Parameters
        -------------
        items: list
            Collection of STAC items returned from API search
        assets: list
            List of red & green band names, 0 index is green and 1 index is NIR band
        bbox: tuple 
            Bounding box coordinates in format (west, south, east, north)

        Returns
        -------------
        xr_stack: xarray.DataArray
            Array with dimensions: time, band, y, x

        """
        print("Generating xarray object")
        xr_stack = stackstac.stack(items, 
                                   assets=assets, 
                                   bounds_latlon=bbox,
                                   chunksize=2048)
        print(f"Data shape: {xr_stack.shape}")
        print(f"Current chunks: {xr_stack.chunks}")
        return xr_stack

    def mean_NDWI(xr_stack, assets): 
        """
        This function finds the mean NDWI for each item

        Parameters: 
        -------------
        xr_stack: xarray.DataArray
            Array with dimensions: time, band, y, x returned from stackstac

        Returns: 
        ------------
        mean: list
            List of means for each scene/time period 
        """
        print("Generating mean NDWI")
        green = xr_stack.sel(band=assets[0])
        nir = xr_stack.sel(band=assets[1])

        ndwi_pixel = (green - nir)/(green + nir)
        ndwi_scene_mean = ndwi_pixel.mean(dim=('y', 'x'))

        return ndwi_scene_mean

    def graph(ndwi_scene_mean): 
        """
        This function plots the mean NDWI for each time. 

        Parameters: 
        --------------
        xr_stack: xarray.DataArray
            Array with dimensions time, band, y, x returned from stackstac
        mean: list
            List of means for each scene/time period

        Returns: 
        -------------
        Scatter plot of mean NDWI for time period. 

        """
        print("Graphing...")
        
        mean_ndwi_values = ndwi_scene_mean.compute() 

        plt.figure(figsize=(10,6))
        ndwi_scene_mean.plot.scatter(marker='o', color='red')

        plt.xlabel('Time')  
        plt.ylabel('Mean NDWI')  
        plt.title('Mean NDWI Over Time')  

        plt.show()  

    items = search_api(api_url, collection, bbox, start_date, end_date)
    xr_stack = create_stackstac(items, assets, bbox)
    ndwi_scene_mean = mean_NDWI(xr_stack, assets)
    graph(ndwi_scene_mean)
    
    return ndwi_scene_mean

    
    