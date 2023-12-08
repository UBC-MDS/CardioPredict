all: docs

# Download, split and preprocess data
data/raw/framingham.csv:
	python scripts/download_data.py --url "https://paulblanche.com/files/framingham.csv" --filepath "data/raw/framingham.csv"

# Split data into train and test sets, preprocess data, and save preprocessor
data/processed/train_data.csv data/processed/X_train.csv data/processed/y_train.csv data/processed/X_test.csv data/processed/y_test.csv results/models/preprocessor.pickle: data/raw/framingham.csv
	python scripts/split_preprocess_data.py --input-file data/raw/framingham.csv --split-dir data/processed/ --preprocess-dir data/processed/ --preprocessor-to results/models/

# Perform EDA and save plots
results/figures/distribution_of_disease_occurrence.png results/figures/age_and_health_indicators_exhibit_elevated_heart_disease.png \
results/figures/correlation_matrix_of_the_features.png results/figures/pairwise_scatter_plot_matrix.png results/figures/distribution_of_the_sex_variable.png \
results/figures/boxplot_of_specified_numerical_features.png : data/processed/train_data.csv
	python scripts/eda.py --df=data/processed/train_data.csv --plot-to=results/figures --data-to=data/processed

# Select model, create and visualize tuning, and save plots
results/tables/result_knn.csv results/figures/accuracy_lines.png results/figures/recall_lines.png: data/processed/X_train.csv data/processed/y_train.csv results/models/preprocessor.pickle
	python scripts/select_knn_model.py --x_train=data/processed/X_train.csv --y_train=data/processed/y_train.csv --preprocessor=results/models/preprocessor.pickle --table-results-to=results/tables --figure-results-to=results/figures

# Train model and save results
results/models/imb_knn_pipeline.pickle results/figures/radar_feature_importance.png: data/processed/X_train.csv data/processed/y_train.csv results/models/preprocessor.pickle
	python scripts/fit_knn_model.py --x_train=data/processed/X_train.csv --y_train=data/processed/y_train.csv --preprocessor=results/models/preprocessor.pickle --pipeline-to=results/models --figure-results-to=results/figures

# Evaluate model on test data and visualize results
results/figures/knn_test_data_confusion_matrix.png results/tables/knn_test_confusion_matrix.csv results/tables/knn_test_data_classification_report.csv: data/processed/X_test.csv data/processed/y_test.csv results/models/imb_knn_pipeline.pickle
	python scripts/knn_eval.py --x_test=data/processed/X_test.csv --y_test=data/processed/y_test.csv --trained_knn_model=results/models/imb_knn_pipeline.pickle --results-dir=results

# Build HTML report and copy build to docs folder
docs: results/knn_evaluation report/_config.yml report/_toc.yml \
	results/figures/distribution_of_disease_occurrence.png \
	results/figures/age_and_health_indicators_exhibit_elevated_heart_disease.png \
	results/figures/correlation_matrix_of_the_features.png \
	results/figures/pairwise_scatter_plot_matrix.png \
	results/figures/distribution_of_the_sex_variable.png \
	results/figures/boxplot_of_specified_numerical_features.png \
	results/figures/radar_feature_importance.png \
	results/tables/result_knn.csv \
	results/figures/accuracy_lines.png \
	results/figures/recall_lines.png \
	results/figures/knn_test_data_confusion_matrix.png \
	results/tables/knn_test_confusion_matrix.csv \
	results/tables/knn_test_data_classification_report.csv \
	results/models/imb_knn_pipeline.pickle 
	jupyter-book build report
	cp -r report/_build/html/* docs

# Clean target to remove generated files
clean:
	rm -f data/raw/framingham.csv
	rm -f data/processed/train_data.csv data/processed/X_train.csv data/processed/y_train.csv data/processed/X_test.csv data/processed/y_test.csv
	rm -f results/models/preprocessor.pickle results/models/imb_knn_pipeline.pickle
	rm -f results/figures/distribution_of_disease_occurrence.png
	rm -f results/figures/radar_feature_importance.png 
	rm -f results/figures/age_and_health_indicators_exhibit_elevated_heart_disease.png
	rm -f results/figures/correlation_matrix_of_the_features.png
	rm -f results/figures/pairwise_scatter_plot_matrix.png
	rm -f results/figures/distribution_of_the_sex_variable.png
	rm -f results/figures/boxplot_of_specified_numerical_features.png
	rm -f results/tables/knn_selection
	rm -f results/knn_evaluation
	rm -rf report/_build/*
	rm -rf docs/*
