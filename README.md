# MSBD540--MH-Risk-Prediction-System
Repository for Summer 2024 MSBD540 project - Mental Health Risk Prediction System

## Overview
This repository contains the predictive modeling project for identifying individuals at high risk of a mental health crisis using the SAMHSA Mental Health Client-Level Data (MH-CLD). The project utilizes machine learning techniques to provide actionable insights that enable healthcare providers to implement preventative measures effectively.

## Project Structure
- `data/`: Directory containing sample datasets. The full SAMHSA MH-CLD dataset can be downloaded at https://www.samhsa.gov/data/data-we-collect/mh-cld-mental-health-client-level-data (data must be compliant with privacy and usage guidelines).
- `src/`: Contains all the source code used for data preprocessing, model training, and evaluation.
  - `preprocess.py`: Script for data cleaning and preprocessing.
  - `train_model.py`: Script for training the predictive model.
  - `evaluate_model.py`: Script for evaluating the model against test data.
  - `risk_prediction.py`: Script for creating risk prediction reports.
- `notebooks/`: Jupyter notebooks
  - `Final_Code.ipynb`: Jupyter notebook containing the exploratory data analysis.
- `docs/`: Documentation related to the project.
  - `Project_Report.pdf`: A comprehensive report summarizing the project's findings.
- `requirements.txt`: A text file listing the project's dependencies.

## Installation
To set up the project environment, follow these steps:
```bash
git clone https://github.com/<link>
pip install -r requirements.txt
