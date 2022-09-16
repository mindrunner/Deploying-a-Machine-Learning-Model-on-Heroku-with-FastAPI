"""
Validate Slices
"""
import csv

from src.ml.data import process_data
from src.ml.model import compute_model_metrics


def validate_model(model, encoder, lb, cat_features, test, path='./model'):
    with open(f'{path}/slices.csv', 'w', encoding='utf-8') as slice_file:
        csv_writer = csv.writer(slice_file)
        header = ['category', 'class', 'precision', 'recall', 'fbeta']
        csv_writer.writerow(header)
        for category in cat_features:
            for cls in test[category].unique():
                data_frame = test[test[category] == cls]
                x_test, y_test, _, _ = process_data(data_frame,
                                                    categorical_features=cat_features,
                                                    training=False,
                                                    label="salary",
                                                    encoder=encoder,
                                                    lb=lb)
                y_pred = model.predict(x_test)
                precision, recall, fbeta = compute_model_metrics(y_test, y_pred)
                csv_writer.writerow([category, cls, precision, recall, fbeta])
