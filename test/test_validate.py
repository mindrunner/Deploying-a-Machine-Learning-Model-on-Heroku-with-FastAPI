import os

from src.train_model import train
from src.validate_model import validate_model


def test_validate(clean_data, cat_features):
    model, encoder, lb = train(clean_data, cat_features, './test/model')

    validate_model(model, encoder, lb, cat_features, clean_data, './test/model')

    assert os.path.isfile("./test/model/slices.csv")
