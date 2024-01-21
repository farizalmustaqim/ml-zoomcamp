FROM python:3.9.7-slim

# Install pipenv
RUN pip install pipenv

# Workdir
WORKDIR /app

# Copy Pipfile and Pipfile.lock files in working dir
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install required packages using pipenv
RUN pipenv install --system --deploy

# copy main.py in the working dir
COPY ["main.py", "./"]

# Expose port 5000
EXPOSE 5000

# Bind the app to
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5000", "main:app"]