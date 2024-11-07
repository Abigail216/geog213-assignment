
## Requirements

You need to have Docker installed on your machine. 


## Instructions

It's recommended to pull the Docker image from Dockerhub. You can also build your own image. 

```
docker pull abphill2004/assignment6:latest
```

```
docker run -it -p 8888:8888 -p 8787:8787 abphill2004/assignment6
```


- Copy the Jupyter Lab url and paste it in your browser. 
- Open `assignment6.ipynb` and follow the instructions. 


Build the Docker image:
- Clone the repository to your local machine
- Change directory to the repository's directory on your machine
- Build the Docker image using the following command:

```
docker build -t assignment6 .
```

- Run the container as following after switching to the repository's directory locally:
```
docker run -it -p 8888:8888 -p 8787:8787 assignment6
```
- Copy the Jupyter Lab url and paste it in your browser. 
- Open `assignment6.ipynb` and follow the instructions. 
