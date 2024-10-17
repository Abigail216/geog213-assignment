## Requirements

You need to have Docker installed on your machine. 


## Instructions

It's recommended to pull the Docker image from Dockerhub. You can also build your own image. 

```
docker pull abphill2004/assignment5:latest
```

```
docker run -it -p 8888:8888 abphill2004/assignment5
```


- Copy the Jupyter Lab url and paste it in your browser. 
- Open `s2_query.ipynb` and follow the instructions. 


Build the Docker image:
- Clone the repository to your local machine
- Change directory to the repository's directory on your machine
- Build the Docker image using the following command:

```
docker build -t assignment5.
```

- Run the container as following after switching to the repository's directory locally:
```
docker run -it -p 8888:8888 assignment5
```
- Copy the Jupyter Lab url and paste it in your browser. 
- Open `s2_query.ipynb' and follow the instructions. 
