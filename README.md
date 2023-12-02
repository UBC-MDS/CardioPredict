<figure>
    <img src="img/CardioPredict.png" alt="Alt text for image" width="800" height="400">
    <figcaption>Created by DALL-E</figcaption>
</figure>

# CardioPredict: Assessing Cardiovascular Disease Risk

![Python](https://img.shields.io/badge/lanaguge-Python-blue.svg)
![codesize](https://img.shields.io/github/languages/code-size/UBC-MDS/DSCI522-Group10)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/UBC-MDS/DSCI522-Group10?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/UBC-MDS/DSCI522-Group10)
![GitHub pull requests](https://img.shields.io/github/issues-pr/UBC-MDS/DSCI522-Group10)
![GitHub](https://img.shields.io/github/license/UBC-MDS/DSCI522-Group10)
![contributors](https://img.shields.io/github/contributors/UBC-MDS/DSCI522-Group10)

> CardioPredict harnesses the power of kNN Models to analyze key health indicators and provide a predictive model for assessing the risk of cardiovascular disease in individuals.

Authors: (listed alphabetically)

Ma, He - UBC-MDS

Gross, Sandy - UBC-MDS

Wang, Doris - UBC-MDS

Wu, Joey - UBC, MDS


# Overview

Cardiovascular disease (CVD) stands as one of the paramount health challenges of our time, being the principal cause of mortality worldwide. The capacity to accurately forecast the onset of CVD is a cornerstone in the endeavor to enhance patient outcomes through timely and effective medical interventions. Our project, CardioPredict, harnesses the power of machine learning to forge a path toward this goal.

Drawing on data from the illustrious Framingham Heart Study (FHS), CardioPredict integrates a spectrum of clinical, demographic, and lifestyle factors to construct a k-Nearest Neighbors (kNN) predictive model. The dataset is a rich tapestry of patient histories, replete with variables that are pivotal in CVD risk assessment.

The crux of our methodology is the meticulous tuning of the kNN algorithm's hyperparameters, ensuring optimal model performance. This is further bolstered by an oversampling technique designed to amplify the model's sensitivity to minority classes, thus addressing inherent class imbalances that often skew predictive outcomes.

While our model achieves moderate accuracy and recall, it brings to light the influential role of both well-known and less-recognized risk factors. Particularly, it identifies cholesterol levels and smoking habits as key predictors of CVD risk, adding to the traditional emphasis on age and blood pressure metrics. These findings are a clarion call for deeper explorations into the multifaceted causes of CVD, with the ultimate aim of honing the precision of our predictive tools.

The journey of CardioPredict does not culminate with the current findings but rather opens new avenues for exploration in the landscape of medical diagnostics. We invite collaborators, researchers, and healthcare professionals to engage with our findings, critique our approach, and contribute to the ongoing enhancement of our model. Together, we can turn the tide against cardiovascular disease and save lives through the power of predictive analytics.

Explore our repository to delve into the intricacies of our analysis, witness the evolution of our model, and partake in our quest to outwit cardiovascular disease.

Final report: [heart_analyis_model.html](https://ubc-mds.github.io/CardioPredict/src/heart_analyis_model.html)

# Installation and Setup

To get started with CardioPredict on your local machine, follow these steps:

## Usage via Virtual Envrionment

First time running the project, run the following from the root of this repository:

```shell
conda env create --file environment.yaml
```

To run the analysis, run the following from the root of this repository:

```shell
conda activate 522-project-disease
jupyter lab 
```

Open `heart_disease_analysis.ipynb` or `heart_analyis_model.ipynb` in Jupyter Lab and under the "Kernel" menu click "Restart Kernel and Run All Cells...".

## Usage via Docker

1. Install Docker
2. Clone the GitHub Repository
   Clone the CardioPredict project repository to your local machine using the following command in your terminal or command prompt:
3. Running the Analysis
   Navigate to the Project Directory
   Use the command line to navigate to the root directory of the cloned CardioPredict project:
   Run the following command to build and start the Docker container:

```shell
docker compose up
```

4. Access Jupyter Lab
   After running the above command, Docker will start Jupyter Lab.
   Look for a URL in the terminal output that starts with [http://127.0.0.1:8888/lab?token=]().
   Copy this URL and paste it into your web browser to access Jupyter Lab.
   Run the Analysis Notebook

   In Jupyter Lab, navigate to and open the heart_analyis_model.ipynb notebook (or the relevant notebook for your analysis).
   To run the analysis, go to the "Kernel" menu in Jupyter Lab, and select "Restart Kernel and Run All Cells...".
5. To reproduce the analysis, run the following commands in the terminal in the project root:

   ```
   # download, split and preprocess data
   python scripts/download_data.py \
   	--url "https://paulblanche.com/files/framingham.csv" \
   	--filepath "data/raw/framingham.csv"

   # split data into train and test sets, preprocess data, and save preprocessor
   python scripts/split_preprocess_data.py \
   	--input-file data/raw/framingham.csv \
   	--split-dir data/processed/ \
   	--preprocess-dir data/processed/ \
   	--preprocessor-to results/models/

   # perform eda and save plots
   python scripts/eda.py \
   	--df=data/processed/train_df.csv
   	--plot-to=results/figures \
   	--data-to=data/processed

   # select model, create visualize tuning, and save plots
   python scripts/select_knn_model.py \
   	--x_train=data/processed/X_train.csv \
   	--y_train=data/processed/y_train.csv \
   	--preprocessor=results/models/preprocessor.pickle  \
   	--table-results-to=results/tables --figure-results-to=results/figures

   # train model and save results
   python scripts/fit_knn_model.py \
   	--x_train=data/processed/X_train.csv \
   	--y_train=data/processed/y_train.csv \
   	--preprocessor=results/models/preprocessor.pickle \
   	--pipeline-to=results/models \
   	--figure-results-to=results/figures

   # evaluate model on test data and visualize results
   python scripts/knn_eval.py \
   	--x_test=data/processed/X_test.csv \
   	--y_test=data/processed/y_test.csv \
   	--trained_knn_model=results/models/imb_knn_pipeline.pickle --results-dir=results

   # build HTML report and copy build to docs folder
   jupyter-book build report
   cp -r report/_build/html/* docs
   ```
6. Clean Up
   To stop the Docker container, go back to your terminal where you launched the container.
   Press Ctrl + C to shut it down.
   Remove the Container

   After shutting down the container, you can remove the stopped containers and associated resources by running:

```shell
docker compose rm
```

## Dependencies

* `conda` (version 23.9.0 or higher)
* `nb_conda_kernels` (version 2.3.1 or higher)
* Python and packages listed in [environment.yaml](environment.yaml)

## Running Tests with pytest

To ensure the reliability and correctness of the functionalities in the CardioPredict project, we have provided comprehensive tests in the [test/](https://github.com/UBC-MDS/CardioPredict/tree/main/tests) directory. To run these tests, simply navigate to the root of the project in your command line interface and execute `pytest`. This command will automatically discover and run all test files located in the [test/ ](https://github.com/UBC-MDS/CardioPredict/tree/main/tests)directory that are designed to validate the code in the [src/](https://github.com/UBC-MDS/CardioPredict/tree/main/src) directory.

# Data

CardioPredict is based on data from the [Framingham Heart Study](https://clinicaltrials.gov/study/NCT00005121), an extensive cohort study that tracks health metrics related to heart disease. The full Framingham dataset, encompassing data from the first 32 clinical exams and event follow-up until 2018, is available upon request from the [National Institutes of Health](https://biolincc.nhlbi.nih.gov/studies/framcohort/). For this project, we utilized a refined subset obtained from [Paul Blanche&#39;s dataset](https://paulblanche.com/files/DataFramingham.html), which contains 1,363 records detailing key health indicators such as age, blood pressure, cholesterol, smoking habits, and occurrences of heart disease.

The dataset includes variables such as age, gender, blood pressure, cholesterol levels, and smoking habits, analyzed to predict the likelihood of developing heart disease.

| Variable | Explanation                                                            |
| -------- | ---------------------------------------------------------------------- |
| sex      | sex (Female/Male)                                                      |
| AGE      | Age in years                                                           |
| FRW      | "Framingham relative weight" (pct.) at baseline (52-222)               |
| SBP      | systolic blood pressure at baseline mmHg (90-300)                      |
| DBP      | diastolic blood pressure at baseline mmHg (50-160)                     |
| CHOL     | cholesterol at baseline mg/100ml (96-430)                              |
| CIG      | cigarettes per day at baseline (0-60)                                  |
| disease  | 1 if coronary heart disease occurred during the follow-up, 0 otherwise |

# Results and Evaluation (rewrite)

The Logistic Regression model achieved an accuracy of 55.3% and a recall of 84%, effectively identifying disease presence but also resulting in many false positives. The class-balanced kNN model showed a recall of 51.7% and an accuracy of 63.7%. The model's performance metrics and graphs are included in the final report.

# Future Work (rewrite)

Future extensions of this project could include exploring more complex models, incorporating more variables, and applying the model to other datasets to validate its robustness.

# References (use Mendeley to recreate)

- Framingham Heart Study. 2023. [https://www.framinghamheartstudy.org/](https://www.framinghamheartstudy.org/)
- National Heart, Lung, and Blood Institute. 2021. Framingham Heart Study Longitudinal Data Documentation for Teaching Dataset. [https://biolincc.nhlbi.nih.gov/media/teachingstudies/FHS_Teaching_Longitudinal_Data_Documentation_2021a.pdf](https://biolincc.nhlbi.nih.gov/media/teachingstudies/FHS_Teaching_Longitudinal_Data_Documentation_2021a.pdf)
- Andersson C, Johnson A D, Benjamin E J, et al. 2019. 70-year legacy of the Framingham Heart Study. Nature Reviews Cardiology, 2019, 16(11): 687-698. [https://www.nature.com/articles/s41569-019-0202-5](https://www.nature.com/articles/s41569-019-0202-5)
- World Heart Report 2023. 2023. World heart report 2023 confronting the world's number one killer.[https://world-heart-federation.org/wp-content/uploads/World-Heart-Report-2023.pdf](https://world-heart-federation.org/wp-content/uploads/World-Heart-Report-2023.pdf)
- World Heart Federation. 2023. Deaths from Cardiovascular Disease Surged 60% Globally Over the Last 30 Years: Report.[https://world-heart-federation.org/news/deaths-from-cardiovascular-disease-surged-60-globally-over-the-last-30-years-report/](https://world-heart-federation.org/news/deaths-from-cardiovascular-disease-surged-60-globally-over-the-last-30-years-report/)
- World Health Organization. 2023. Cardiovascular diseases (CVDs). [https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)](https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds))

# License

This project is released under [MIT License](https://opensource.org/license/mit/).
