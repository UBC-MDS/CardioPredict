<figure>
    <img src="img/CardioPredict.png" alt="Alt text for image" width="800" height="400">
    <figcaption>Created by DALL-E</figcaption>
</figure>

# CardioPredict: Assessing Cardiovascular Disease Risk

![Python](https://img.shields.io/badge/language-Python-blue.svg)
![codesize](https://img.shields.io/github/languages/code-size/UBC-MDS/DSCI522-Group10)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/UBC-MDS/DSCI522-Group10?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/UBC-MDS/DSCI522-Group10)
![GitHub pull requests](https://img.shields.io/github/issues-pr/UBC-MDS/DSCI522-Group10)
![contributors](https://img.shields.io/github/contributors/UBC-MDS/DSCI522-Group10)

> CardioPredict harnesses the power of kNN Models to analyze key health indicators and provide a predictive model for assessing the risk of cardiovascular disease in individuals.

Authors: (listed alphabetically)

Gross, Sandy - UBC-MDS

Ma, He - UBC-MDS

Wang, Doris - UBC-MDS

Wu, Joey - UBC-MDS

# Overview

Cardiovascular disease (CVD) stands as one of the paramount health challenges of our time, being the principal cause of mortality worldwide. The capacity to accurately forecast the onset of CVD is a cornerstone in the endeavor to enhance patient outcomes through timely and effective medical interventions. Our project, CardioPredict, harnesses the power of machine learning to forge a path toward this goal.

Drawing on data from the illustrious Framingham Heart Study (FHS), CardioPredict integrates a spectrum of clinical, demographic, and lifestyle factors to construct a k-Nearest Neighbors (kNN) predictive model. The dataset is a rich tapestry of patient histories, replete with variables that are pivotal in CVD risk assessment.

The crux of our methodology is the meticulous tuning of the kNN algorithm's hyperparameters, ensuring optimal model performance. This is further bolstered by an oversampling technique designed to amplify the model's sensitivity to minority classes, thus addressing inherent class imbalances that often skew predictive outcomes.

While our model achieves moderate accuracy (62.2%) )and recall (55.2%), it brings to light the influential role of both well-known and less-recognized risk factors. Particularly, it identifies cholesterol levels and smoking habits as key predictors of CVD risk, adding to the traditional emphasis on age and blood pressure metrics. These findings are a clarion call for deeper explorations into the multifaceted causes of CVD, with the ultimate aim of honing the precision of our predictive tools.

# Community Guidelines

The journey of CardioPredict does not culminate with the current findings but rather opens new avenues for exploration in the landscape of medical diagnostics. We invite collaborators, researchers, and healthcare professionals to engage with our findings, critique our approach, and contribute to the ongoing enhancement of our analysis.

Explore our repository to delve into the intricacies of our analysis, witness the evolution of our model, and partake in our quest to outwit cardiovascular disease. If you're looking to contribute to the project, we welcome your interest! Please start by reading our CONTRIBUTING.md file for details on how to submit pull requests, and we recommend you to discuss your proposed changes with us via issues before starting to work on them. Found a bug or have a feature request? We value your input! Please log an issue on our GitHub repository with a clear title and a detailed description. Ensure to check existing issues to avoid duplicates and provide steps to reproduce the issue, if applicable. For any questions or support requests, please use the Issues section of our GitHub repository. Provide as much context as possible to help us understand and address your query promptly.

Final report: [Link](https://ubc-mds.github.io/CardioPredict/heart_analysis_report.html)

# Installation and Setup

To get started with CardioPredict on your local machine, follow these steps:

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
   	--df=data/processed/train_data.csv \
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
## Running the analysis
To replicate the analysis, you can run the following command from the root directory of this project:
```shell
docker-compose run --rm disease_pred make all
```
To reset the repository to its original clean state, run the following command from the root directory of this project:
```shell
docker-compose run --rm disease_pred make clean
```

## Dependencies

* `conda` (version 23.9.0 or higher)
* `nb_conda_kernels` (version 2.3.1 or higher)
* Python and packages listed in [environment.yaml](https://github.com/UBC-MDS/CardioPredict/blob/main/environment.yaml)

## Running Tests with pytest

To ensure the reliability and correctness of the functionalities in the CardioPredict project, we have provided comprehensive tests in the [test/](https://github.com/UBC-MDS/CardioPredict/tree/main/tests) directory. To run these tests, simply navigate to the root of the project in your command line interface and execute `pytest`. This command will automatically discover and run all test files located in the [test/ ](https://github.com/UBC-MDS/CardioPredict/tree/main/tests)directory that are designed to validate the code in the [src/](https://github.com/UBC-MDS/CardioPredict/tree/main/src) directory.

# Data

CardioPredict is based on data from the renowned Framingham Heart Study (FHS), an extensive cohort study that tracks health metrics related to heart disease. The full Framingham dataset, encompassing data from the first 32 clinical exams and event follow-up until 2018, is available upon request from the [National Institutes of Health](https://biolincc.nhlbi.nih.gov/studies/framcohort/). For this project, we utilized a refined subset from Professor Paul Blanche ([dataset](https://paulblanche.com/files/DataFramingham.html)), which contains 1,363 records detailing key health indicators such as age, blood pressure, cholesterol, smoking habits, and occurrences of heart disease.

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

# Results and Evaluation

This analysis has refined the k-Nearest Neighbors (kNN) model for cardiovascular disease prediction, showcasing that oversampling significantly improves recall-a primary focus of our research-especially with a lower number of neighbors, while maintaining reasonable accuracy. Choosing nine neighbors strikes a balance between complexity and generalization, avoiding overfitting and ensuring reliable recall, which is vital for medical diagnostics. A permutation-based analysis revealed AGE (age) and SBP (systolic blood pressure) as critical predictors, along with CHOL (cholesterol levels) and CIG (cigarette consumption), indicating a complex interplay of risk factors. The observed modest levels of overall accuracy (62.2%)and recall (55.2%) highlight the need for further methodological improvements.  These insights underline the potential of our model to inform clinical practice, enhancing personalized patient care despite the presence of false negatives and positives, which point to areas for future improvement. The final report includes detailed metrics and graphical representations of the model's performance.

# Future Work

Future work will prioritize advancing our cardiovascular disease diagnostic model through a comprehensive, multifaceted approach. This will involve incorporating a broader range of clinical data, such as cholesterol levels and smoking habits, which have proven significant in our analyses. Additionally, we aim to refine the model's accuracy and recall by employing advanced algorithmic techniques and cost-sensitive learning frameworks, ensuring a delicate balance between sensitivity and specificity. These efforts are crucial for optimizing the model's performance in real-world clinical settings, addressing the economic and human costs of false diagnoses, and ultimately enhancing patient care and outcomes.

# References

li, M. M., Paul, B. K., Ahmed, K., Bui, F. M., Quinn, J. M. W., & Moni, M. A. (2021). Heart disease prediction using supervised machine learning algorithms: Performance analysis and comparison.  *Computers in Biology and Medicine* ,  *136* , 104672. https://doi.org/10.1016/J.COMPBIOMED.2021.104672

Andersson, C., Johnson, A. D., Benjamin, E. J., Levy, D., & Vasan, R. S. (2019). 70-year legacy of the Framingham Heart Study.  *Nature Reviews Cardiology 2019 16:11* ,  *16* (11), 687–698. [https://doi.org/10.1038/s41569-019-0202-5](https://doi.org/10.1038/s41569-019-0202-5)

Andersson, C., Nayor, M., Tsao, C. W., Levy, D., & Vasan, R. S. (2021). Framingham Heart Study: JACC Focus Seminar, 1/8.  *Journal of the American College of Cardiology* ,  *77* (21), 2680–2692. [https://doi.org/10.1016/J.JACC.2021.01.059](https://doi.org/10.1016/J.JACC.2021.01.059)

Barden, A. E., Huang, R. C., Beilin, L. J., Rauschert, S., Tsai, I. J., Oddy, W. H., & Mori, T. A. (2022). Identifying young adults at high risk of cardiometabolic disease using cluster analysis and the Framingham 30-yr risk score.  *Nutrition, Metabolism and Cardiovascular Diseases* ,  *32* (2), 429–435. [https://doi.org/10.1016/J.NUMECD.2021.10.006](https://doi.org/10.1016/J.NUMECD.2021.10.006)

 *BioLINCC: Framingham Heart Study-Cohort (FHS-Cohort)* . (n.d.). Retrieved November 29, 2023, from https://biolincc.nhlbi.nih.gov/studies/framcohort/

 *Cardiovascular diseases (CVDs)* . (n.d.). Retrieved November 29, 2023, from [https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)](https://www.who.int/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds))

Cherif, W. (2018). Optimization of K-NN algorithm by clustering and reliability coefficients: application to breast-cancer diagnosis.  *Procedia Computer Science* ,  *127* , 293–299. [https://doi.org/10.1016/J.PROCS.2018.01.125](https://doi.org/10.1016/J.PROCS.2018.01.125)

DAWBER, T. R., MEADORS, G. F., & MOORE, F. E. (1951). Epidemiological Approaches to Heart Disease: The Framingham Study.  *American Journal of Public Health and the Nations Health* ,  *41* (3), 279. [https://doi.org/10.2105/AJPH.41.3.279](https://doi.org/10.2105/AJPH.41.3.279)

DAWBER, T. R., MOORE, F. E., & MANN, G. V. (1957). Coronary heart disease in the Framingham study.  *American Journal of Public Health and the Nation’s Health* ,  *47* (4 Pt 2), 4–24. [https://doi.org/10.2105/AJPH.47.4_PT_2.4](https://doi.org/10.2105/AJPH.47.4_PT_2.4)

 *Deaths from cardiovascular disease surged 60% globally over the last 30 years: Report - World Heart Federation* .
(n.d.). Retrieved November 29, 2023, from [https://world-heart-federation.org/news/deaths-from-cardiovascular-disease-surged-60-globally-over-the-last-30-years-report/](https://world-heart-federation.org/news/deaths-from-cardiovascular-disease-surged-60-globally-over-the-last-30-years-report/)

 *Framingham data* . (n.d.). Retrieved November 29, 2023, from https://paulblanche.com/files/DataFramingham.html

jabbar, M. A., Deekshatulu, B. L., & Chandra, P. (2013). Classification of Heart Disease Using K-Nearest Neighbor and Genetic Algorithm.  *Procedia Technology* ,  *10* , 85–94. [https://doi.org/10.1016/J.PROTCY.2013.12.340](https://doi.org/10.1016/J.PROTCY.2013.12.340)

Lahmiri, S. (2023). Integrating convolutional neural networks, kNN, and Bayesian optimization for efficient diagnosis of Alzheimer’s disease in magnetic resonance images.  *Biomedical Signal Processing and Control* ,  *80* , 104375. https://doi.org/10.1016/J.BSPC.2022.104375

 *National Heart, Lung, and Blood Institute. 2021. Framingham Heart Study Longitudinal Data Documentation for Teaching Dataset* .
(n.d.). Retrieved November 29, 2023, from https://biolincc.nhlbi.nih.gov/media/teachingstudies/FHS_Teaching_Longitudinal_Data_Documentation_2021a.pdf

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, É. (2012). Scikit-learn: Machine Learning in Python.  *Journal of Machine Learning Research* ,  *12* , 2825–2830. [https://arxiv.org/abs/1201.0490v4](https://arxiv.org/abs/1201.0490v4)

 *Study Details | Framingham Heart Study | ClinicalTrials.gov* . (n.d.). Retrieved November 29, 2023, from [https://clinicaltrials.gov/study/NCT00005121](https://clinicaltrials.gov/study/NCT00005121)

Sun, X., Ho, J. E., Gao, H., Evangelou, E., Yao, C., Huan, T., Hwang, S. J., Courchesne, P., Larson, M. G., Levy, D., Ma, J., & Liu, C. (2021). Associations of Alcohol Consumption with Cardiovascular Disease-Related Proteomic Biomarkers: The Framingham Heart Study.  *The Journal of Nutrition* ,  *151* (9), 2574–2582. [https://doi.org/10.1093/JN/NXAB186](https://doi.org/10.1093/JN/NXAB186)

Tsao, C. W., & Vasan, R. S. (2015). The Framingham Heart Study: past, present and future.  *International Journal of Epidemiology* ,  *44* (6), 1763–1766. [https://doi.org/10.1093/IJE/DYV336](https://doi.org/10.1093/IJE/DYV336)

 *World Heart Report 2023: Full Report - World Heart Federation* . (n.d.). Retrieved November 29, 2023, from [https://world-heart-federation.org/resource/world-heart-report-2023/](https://world-heart-federation.org/resource/world-heart-report-2023/)

# License

The CadioPredict report contained herein are licensed under the [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) License](https://creativecommons.org/licenses/by-nc-sa/4.0/). See [the license file](https://github.com/UBC-MDS/CardioPredict/blob/main/LICENSE) for more information. If re-using/re-mixing please provide attribution and link to this webpage. The software code contained within this repository is licensed under the MIT license. See [the license file](https://github.com/UBC-MDS/CardioPredict/blob/main/LICENSE) for more information.
