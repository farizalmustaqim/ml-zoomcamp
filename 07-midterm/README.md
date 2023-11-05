# Stroke Prediction with Machine Learning

## Introduction
Stroke is a disease that occurs when the blood supply to part of your brain is interrupted or reduced, preventing brain tissue from getting oxygen and nutrients. Brain cells begin to die in minutes. A stroke is a medical emergency, and prompt treatment is crucial. Early action can reduce brain damage and other complications. The good news is that strokes can be treated and prevented, and many fewer Americans die of stroke now than in the past. 

## Business Problem
Stroke is a disease that can be prevented. The goal of this project is to build a machine learning model to predict whether a patient is likely to get a stroke or not. The model will be used to identify patients with a high risk of stroke so that they can get early treatment to prevent the stroke. 

## Data
The data is from Kaggle: https://www.kaggle.com/fedesoriano/stroke-prediction-dataset

## Exploring the model in notebook
The notebook is available in this repository: **notebook.ipynb**

## How to train the model
1. Clone this repository
2. Download the data from Kaggle and save it to same directory as the repository
3. Install the requirements with pipenv `pipenv install`
4. Activate the virtual environment `pipenv shell`
5. Run the training script `python train.py`

## Docker
1. Clone this repository
2. Download the data from Kaggle and save it to same directory as the repository
3. Build the docker image `docker build -t stroke-prediction .`
4. Run the docker image `docker run -it -p 8000:8000 stroke-prediction:latest`


