# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

The model is created with a RandomForestClassifier with its default settings.

## Intended Use

The model can be used to predict whether a person has a higher salary of 50k or a lower one.

## Training Data

Source: https://archive.ics.uci.edu/ml/datasets/census+income
The data is split with `train_test_split`. 80% is used for training

## Evaluation Data

Source: https://archive.ics.uci.edu/ml/datasets/census+income
The data is split with `train_test_split`. 20% is used for evaluation

## Metrics

Model evaluation was being done by:
- Accuracy Score
- F1 beta score
- Precision
- Recall

Values are about `0.6` in average

## Ethical Considerations

Model Contain Race and Gender values and might discriminate people. Evaluation of that was not scope of this project.

## Caveats and Recommendations

No stratification was applied on the data. There might be a strong bias on gender, race or other categories