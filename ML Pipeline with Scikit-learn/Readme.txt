Task 2: End-to-End ML Pipeline for Customer Churn Prediction

Objective:
To build a reusable and production-ready machine learning pipeline capable of predicting customer churn. The task demonstrates the ability to preprocess data, train multiple models, tune hyperparameters, and deploy ML pipelines.

Dataset:
Telco Customer Churn dataset, containing customer demographic and service usage data along with a churn label.

Methodology:
1. Data Preprocessing:
   - Handling missing values
   - One-hot encoding of categorical variables
   - Feature scaling using StandardScaler

2. ML Pipeline Construction:
   - Implemented using scikit-learn Pipeline API
   - Integrated preprocessing steps and model training
   - Models: Logistic Regression, Random Forest Classifier

3. Hyperparameter Tuning:
   - GridSearchCV applied for parameter optimization
   - Evaluation using cross-validation metrics (accuracy, F1-score)

4. Pipeline Export:
   - Exported trained pipeline using joblib for reuse in production
   - Ensures consistency in preprocessing and prediction

Key Results / Observations:
- Logistic Regression achieved competitive accuracy with interpretability
- Random Forest improved predictive performance on complex patterns
- The pipeline can be reused directly for new customer datasets

Skills Gained:
- ML pipeline construction and reusability
- Hyperparameter tuning using GridSearchCV
- Model export and production readiness