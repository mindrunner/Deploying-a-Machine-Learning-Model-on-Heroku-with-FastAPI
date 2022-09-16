import os

from src.train_model import train


def test_train(clean_data, cat_features):
    train(clean_data, cat_features, './test/model')

    assert os.path.isfile("./test/model/model.joblib")
    assert os.path.isfile("./test/model/encoder.joblib")
    assert os.path.isfile("./test/model/lb.joblib")
