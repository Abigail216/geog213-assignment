FROM continuumio/miniconda3:22.11.1

# Create a Conda environment with Python 3.8
RUN conda create -n myenv python=3.8

# Install required packages
RUN conda run -n myenv conda install numpy=1.23.1 jupyterlab=3.6.3 matplotlib=3.7.2
RUN conda run -n myenv conda install pystac-client=0.7.5 --channel conda-forge

# Activate environment
RUN echo "conda activate myenv" >> ~/.bashrc
ENV PATH="/opt/conda/envs/myenv/bin:$PATH"

# Create a non-root user and switch to that user
RUN useradd -m jupyteruser
RUN chown -R jupyteruser:jupyteruser /home/jupyteruser


# Copy files into the image
COPY --chown=jupyteruser:jupyteruser s2_query.ipynb /home/jupyteruser/

USER jupyteruser
WORKDIR /home/jupyteruser

# Expose the JupyterLab port
EXPOSE 8888

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]