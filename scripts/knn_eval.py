import click
import pandas as pd
import pickle
from sklearn.metrics import confusion_matrix, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import os

@click.command()
@click.option('--x_test', default = 'data/processed/X_test.csv', type=str, help="Path to X_test")
@click.option('--y_test',default = 'data/processed/y_test.csv',type=str, help="Path to y_test")
@click.option('--trained_knn_model', default ='results/models/imb_knn_pipeline.pickle', type=str, help="Path to the trained knn model pipeline")
@click.option('--results-dir',default ='results', type=str, help="Directory to save the evaluation results")

def main(x_test, y_test, trained_knn_model, results_dir):
    # Load test data
    X_test = pd.read_csv(x_test)
    y_test = pd.read_csv(y_test).squeeze()

    # Load the trained model pipeline
    with open(trained_knn_model, 'rb') as f:
        knn = pickle.load(f)

    # Make predictions
    y_pred = knn.predict(X_test)


    # Prepare directories for saving figures and tables
    figures_path = os.path.join(results_dir, 'figures')
    tables_path = os.path.join(results_dir, 'tables')
    os.makedirs(figures_path, exist_ok=True)
    os.makedirs(tables_path, exist_ok=True)

    # Compute confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    fig, ax = plt.subplots(figsize=(10,10))
    disp.plot(ax=ax)
    plt.savefig(os.path.join(figures_path, 'knn_test_data_confusion_matrix.png'))

    # Generate classification report
    report = classification_report(y_test, y_pred, output_dict=True, zero_division=1)
    report_df = pd.DataFrame(report).transpose()
    report_df.to_csv(os.path.join(tables_path, 'knn_test_data_classification_report.csv'))


if __name__ == '__main__':
    main()
# python scripts/knn_eval.py --x_test=data/processed/X_test.csv --y_test=data/processed/y_test.csv --trained_knn_model=results/models/imb_knn_pipeline.pickle --results-dir=results
