FROM python:3.9.5-slim-buster

# Install pipenv
RUN pip install pipenv

# Set the working directory to /app
WORKDIR /app

# Copy pipfile and pipfile.lock to the working directory
COPY ["Pipfile", "Pipfile.lock", "./"]

# install the pipenv dependencies for the project and deploy them.
RUN pipenv install --system --deploy

# Copy any python files and the model we had to the working directory of Docker 
COPY ["*.py", "random_forest.bin", "./"]

# We need to expose the 9696 port because we're not able to communicate with Docker outside it
EXPOSE 8000

# If we run the Docker image, we want our churn app to be running
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "predict:app"]
