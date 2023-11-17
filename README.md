<img src="img/CardioPredict.png" alt="Alt text for image" width="800" height="400">

    Image created by DALL-3

# CardioPredict: Assessing Heart Disease Risk

![Python](https://img.shields.io/badge/lanaguge-Python-blue.svg)
![codesize](https://img.shields.io/github/languages/code-size/UBC-MDS/DSCI522-Group10)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/UBC-MDS/DSCI522-Group10?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/UBC-MDS/DSCI522-Group10)
![GitHub pull requests](https://img.shields.io/github/issues-pr/UBC-MDS/DSCI522-Group10)
![GitHub](https://img.shields.io/github/license/UBC-MDS/DSCI522-Group10)
![contributors](https://img.shields.io/github/contributors/UBC-MDS/DSCI522-Group10)

> CardioPredict harnesses the power of logistic regression to analyze key health indicators and provide a predictive model for assessing the risk of coronary heart disease in individuals.

Author: Joey Wu, He Ma, Sandy Gross and Doris Wang

# Project Overview

CardioPredict leverages logistic regression analysis to evaluate key health indicators for predicting coronary heart disease risk. This project aims to create a reliable predictive model using data from the Framingham Heart Study, enhancing our understanding of heart disease risk factors. + a little more introduction.

Final report: link here.

# Installation and Setup

To get started with CardioPredict on your local machine, follow these steps:

## Usage

First time running the project, run the following from the root of this repository:

```shell
conda env create --file environment.yml
```

To run the analysis, run the following from the root of this repository:

```shell
conda activate breast_cancer_predictor
jupyter lab 
```

Open `src/breast_cancer_predict_report.ipynb` in Jupyter Lab and under the "Kernel" menu click "Restart Kernel and Run All Cells...".

## Dependencies

* `conda` (version 23.9.0 or higher)
* `nb_conda_kernels` (version 2.3.1 or higher)
* Python and packages listed in (link of the yml file)

# Data

CardioPredict is based on data from the [Framingham Heart Study](https://clinicaltrials.gov/study/NCT00005121), an extensive cohort study that tracks health metrics related to heart disease. The full Framingham dataset, encompassing data from the first 32 clinical exams and event follow-up until 2018, is available upon request from the [National Institutes of Health](https://biolincc.nhlbi.nih.gov/studies/framcohort/).

## Source Data

 For this project, we utilized a refined subset obtained from [Paul Blanche's dataset](https://paulblanche.com/files/DataFramingham.html), which contains 1,363 records detailing key health indicators such as age, blood pressure, cholesterol, smoking habits, and occurrences of heart disease.

## Data Overiew

The dataset includes variables such as age, gender, blood pressure, cholesterol levels, and smoking habits, analyzed to predict the likelihood of developing heart disease.

Some EDA visual images here.

# Code structure (optional)

The project is structured as follows:

```bash
├── data
│   └── framingham.csv
├── data_acquisition.py
├── data_preprocessing.ipynb
├── data_analysis.ipynb
├── data_modelling.ipynb
├── Img
│   └── CardioPredict.png
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── environment.yml  
├── LICENSE
├── README.md
└── .gitignore
```

# Results and Evaluation

The logistic regression model shows promising results in predicting heart disease risk, with an accuracy of [X%]. The model's performance metrics and graphs are included in the final report.

# Future Work

Future extensions of this project could include exploring more complex models, incorporating more variables, and applying the model to other datasets to validate its robustness.

# References

- Framingham Heart Study [https://www.framinghamheartstudy.org/](https://www.framinghamheartstudy.org/)
- Framingham Heart Study Longitudinal Data Documentation for Teaching Dataset [https://biolincc.nhlbi.nih.gov/media/teachingstudies/FHS_Teaching_Longitudinal_Data_Documentation_2021a.pdf](https://biolincc.nhlbi.nih.gov/media/teachingstudies/FHS_Teaching_Longitudinal_Data_Documentation_2021a.pdf)
- Andersson C, Johnson A D, Benjamin E J, et al. 70-year legacy of the Framingham Heart Study[J]. Nature Reviews Cardiology, 2019, 16(11): 687-698. [https://www.nature.com/articles/s41569-01](https://www.nature.com/articles/s41569-019-0202-5)
- World Heart Report 2023[https://world-heart-federation.org/wp-content/uploads/World-Heart-Report-2023.pdf](https://world-heart-federation.org/wp-content/uploads/World-Heart-Report-2023.pdf)

# License

This project is released under [MIT License](https://opensource.org/license/mit/).
