# Tutorial for how to run a container from Dockerfile and execute the Jupyter Notebook

## Requirements

You need to have Docker installed on your machine. 

## Instructions
- Clone the repository to your local machine
- Change directory to the repository's directory on your machine
- Build the Docker image using the following command:
```
docker build -t assignment4 .
```
- Run a container using the following command:
```
docker run -p 8888:8888 -v $(pwd):/home/assignment assignment
```
- Copy the Jupyter Lab url and paste it in your browser. 
- Open `A4_notebook.ipynb`
- Once the notebook is open, run the cells by clicking the run button. 