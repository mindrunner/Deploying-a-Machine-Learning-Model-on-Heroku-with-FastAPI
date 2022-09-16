import logging
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from src.cat_features import cat_features
from src.train_model import train
from src.validate_model import validate_model

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

data = pd.read_csv('./data/clean_census.csv')

train_data, test_data = train_test_split(data, test_size=0.20)

model, encoder, lb = train(train_data, cat_features)
validate_model(model, encoder, lb, cat_features, test_data)
