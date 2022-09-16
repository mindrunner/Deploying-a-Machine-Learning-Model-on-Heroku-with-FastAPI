import pandas as pd
import pytest


@pytest.fixture
def clean_data():
    """
    Get data
    """
    return pd.read_csv('./data/clean_census.csv')

@pytest.fixture
def cat_features():
    """
    Get cat_features
    """

    return [
        "workclass",
        "education",
        "marital_status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native_country",
    ]


@pytest.fixture
def inference_data_lte():
    data = {'age': 40,
            'workclass': 'Private',
            'fnlgt': 237645,
            'education': 'HS-grad',
            'marital_status': 'Separated',
            'occupation': 'Tech-support',
            'relationship': 'Unmarried',
            'race': 'Other',
            'sex': 'Female',
            'capital_gain': 0,
            'capital_loss': 0,
            'hours_per_week': 20,
            'native_country': 'Poland'}
    return pd.DataFrame(data, index=[0])


@pytest.fixture
def inference_data_gt():
    data = {'age': 55,
            'workclass': 'Self-emp-inc',
            'fnlgt': 458743,
            'education': 'Doctorate',
            'marital_status': 'Never-married',
            'occupation': 'Prof-specialty',
            'relationship': 'Wife',
            'race': 'White',
            'sex': 'Male',
            'capital_gain': 0,
            'capital_loss': 0,
            'hours_per_week': 40,
            'native_country': 'United-States'}

    return pd.DataFrame(data, index=[0])
