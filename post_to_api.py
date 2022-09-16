import requests

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

response = requests.post(url='https://machine-learning-fastapi.herokuapp.com/', json=payload)

print(response.status_code)
print(response.json())
