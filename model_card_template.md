# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Model Type: Random Forest Classifier
Model Description: This model is trained to predict income level (either >50K or <=50K) based on demographic and employment-related features from the Census dataset. 

## Intended Use
The model is intended to predict whether an individual's income is greater than 50K or less than or equal to 50K.

## Training Data
Data Source: The model was trained on the census.csv dataset
Data Description: The dataset contains demographic and employment-related information, including features like age, work class, education, marital status, occupation, race, sex, and native country. The target variable is income level is either >50K or <=50K

## Evaluation Data
The "census.csv" dataset was split using Stratified K-Fold cross-validation (5 splits). The evaluation data is 1/5th of the total dataset, held out from training in each fold.

## Metrics
Model Training: F1, Precision, Recall
Precision: 0.7403 | Recall: 0.6214 | F1: 0.6757

## Ethical Considerations
The model appears to be biased towards higher education levels, certain occupations, and potentially certain marital statuses. This could lead to unfair predictions and perpetuate existing inequalities

## Caveats and Recommendations
The model's performance should be monitored over time, and it should be retrained with updated data to ensure continued accuracy and fairness