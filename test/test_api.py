from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "running"}


def test_pred_salary_gt():
    payload = {'age': 55,
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

    response = client.post("/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"salary": ">50k"}


def test_pred_salary_lte():
    payload = {'age': 40,
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

    response = client.post("/", json=payload)
    assert response.status_code == 200
    assert response.json() == {"salary": "<=50k"}
