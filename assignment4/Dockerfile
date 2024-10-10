FROM continuumio/miniconda3:24.7.1-0

# Copy the environment.yml file into the container
COPY environment.yml /home/environment.yml

# Create a Conda env from environment.yml
RUN conda env create -f /home/environment.yml

# Activate the conda environment
RUN echo "conda activate a4-env" >> ~/.bashrc
ENV PATH="$PATH:/opt/conda/envs/a4-env/bin"

#Create a non-root user and switch to that user
RUN useradd -m assignment
USER assignment

# Set the working directory to /home/assignment
WORKDIR /home/assignment

# Expose the JupyterLab port
EXPOSE 8888

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0"]