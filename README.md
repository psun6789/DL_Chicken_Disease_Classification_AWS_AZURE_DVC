# ML_DL_Projects
# Project Name: Chicken Disease Image Classification
# Dataset Link : https://www.kaggle.com/datasets/efoeetienneblavo/chicken-disease-dataset?select=chicken_disease

1. UPDATE config.yaml
2. UPDATE secrets.yaml (#-->optional)
3. UPDATE params.yaml
4. UPDATE the entity
5. UPDATE the configuration manager in src config
6. UPDATE the components
7. UPDATE the pipeline
8. UPDATE the main.py
9. UPDATE dvc.yaml

Steps to RUN

1. Clone Repo
https://github.com/psun6789/DL_Chicken_Disease_Classification_AWS_AZURE_DVC.git

2. Create Virtual Environment
conda create --name VIRTUAL_ENV python==3.9

<!-- To run DVC pipeline -->
dvc repro 
<!-- DVC Relationship -->
dvc dag



<!-- ERC Repo to store/save docker Image -->
851725536163.dkr.ecr.eu-north-1.amazonaws.com/chicken_disease_classification
