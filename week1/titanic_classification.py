import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Dataset load
df = pd.read_csv("titanic.csv")

# Required columns
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']]

# Missing values handle
df['Age'] = df['Age'].fillna(df['Age'].median())

# Convert text to numbers
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Features and Target
X = df.drop('Survived', axis=1)
y = df['Survived']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Results
print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions))