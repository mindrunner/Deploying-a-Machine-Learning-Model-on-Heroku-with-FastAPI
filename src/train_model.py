"""
Train Model
"""

from joblib import dump

from src.ml.data import process_data
from src.ml.model import train_model


def train(train_data, features, out='./model'):
    x_train, y_train, encoder, lb = process_data(
        train_data, categorical_features=features, label="salary", training=True
    )

    model = train_model(x_train, y_train)
    dump(model, f"{out}/model.joblib")
    dump(encoder, f"{out}/encoder.joblib")
    dump(lb, f"{out}/lb.joblib")

    return model, encoder, lb
