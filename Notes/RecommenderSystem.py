import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#This code is to detect "Fradulent" Transactions in a Reccomender System.
#We load the dataset and split it into training and testing sets.

#We create a Random Forest classifier and train it on the training data.

#We make predictions on the test set and evaluate the model's performance using a classification report, confusion matrix, and accuracy score.

# Load your dataset (assuming it contains features and a label indicating fraud or not)
data = pd.read_csv('credit_card_transactions.csv')

# Split the dataset into training and testing sets
X = data.drop('label', axis=1)
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a Random Forest classifier
rf_classifier = RandomForestClassifier(random_state=42)
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the model's performance
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Accuracy Score:")
print(accuracy_score(y_test, y_pred))
