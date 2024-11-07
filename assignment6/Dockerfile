FROM continuumio/miniconda3:24.7.1-0

RUN conda create -n assignment6 python=3.10

RUN conda run -n assignment6 conda install jupyterlab=4.2.5 \
    pystac-client\
    dask\
    dask-labextension\
    distributed\
    rioxarray\
    gdal\
    planetary-computer\
    stackstac\
    matplotlib\
    sqlite\
    matplotlib --channel conda-forge

# Activate the Conda environment
RUN echo "conda activate assignment6" >> ~/.bashrc
ENV PATH="$PATH:/opt/conda/envs/assignment6/bin"

# Create a non-root user and switch to that user
RUN useradd -m jupyteruser
USER jupyteruser

WORKDIR /home/jupyteruser
COPY tools.py .
COPY Dockerfile .
COPY assignment6.ipynb .

# Expose the JupyterLab port
EXPOSE 8888

# Expose the Dask Dashboard port
EXPOSE 8787

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0"]