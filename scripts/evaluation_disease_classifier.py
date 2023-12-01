import click
import os
import pandas as pd
import pickle
from sklearn.metrics import recall_score
from sklearn.metrics import ConfusionMatrixDisplay

@click.command()
@click.option('--X-test', type=str, help="Path to X_test")
@click.option('--y-test', type=str, help="Path to y_test")
@click.option('--model-from', type=str, help="Path to directory where the fit pipeline object of your desired modellives")
@click.option('--plot-to', type=str, help="Path to directory where the result plot will be written to")
@click.option('--matrix-to', type=int, help="Path to directory where the result matrix will be written to")

def main(X_test, y_test, model_from, plot_to, matrix_to):
        "Evaluated fitted pipeline on test data and save the results as a Matrix and DataFrame"

        #load X_test and y_test
        X_test = pd.read_csv(X_test)
        y_test = pd.read_csv(y_test)

        #load fitted pipeline
        with open(pipeline_from, 'rb') as f:
        lr_disease_fit = pickle.load(f)

        #score pipeline on test data and save the results
        accuracy_test = lr_disease_fit.score(X_test, y_test)
        recall_test = recall_score(y_test, lr_disease_fit.predict(X_test), pos_label=1)
        result_test = pd.DataFrame({'accuracy_test':accuracy_test, 'recall_test': recall_test}))
        result_test.to_csv(os.path.join(matrix_to, "test_results.csv"), index=False)

        #Create Confusion matrix
        confusion_matrix = ConfusionMatrixDisplay.from_predictions(
        y_test,  
        lr_disease_fit.predict(X_test)
        )
        #Export Confusion Matrix
        confusion_matrix.save(os.path.join(plot_to, "confusion_matrix_test.png"),
              scale_factor=2.0)
