import utils
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE


dataset = utils.read_dataset("binary_classification_cleaned.csv")

#print(dataset.head())

dataset["positionOrder"] = (dataset["positionOrder"] < 4).astype(int)

#print(dataset["positionOrder"].value_counts())

X = dataset.drop(columns = "positionOrder")
y = dataset["positionOrder"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

smote = SMOTE(random_state = 42)
x_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

#print(y_train_smote.value_counts())

model = RandomForestClassifier(n_estimators = 100, class_weight = "balanced", random_state = 42)
model.fit(x_train_smote, y_train_smote)

y_pred = model.predict(X_test)

print(f"Accuracy: {classification_report(y_test, y_pred)}")


""" 
Before SMOTE:
        precision    recall  f1-score   support
0       0.94         0.96      0.95      1729
1       0.76         0.67      0.71       322

After SMOTE:
        precision    recall  f1-score   support
0       0.96         0.93      0.94      1729
1       0.67         0.80      0.73       322

"""