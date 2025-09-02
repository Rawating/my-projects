import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


input_wlb = input("Enter your WorkLifeBalanceScore: ")
input_mss= input("Enter your ManagerSupportScore: ")
input_js = input("Enter your JobSatisfaction: ")
# Load data
health_data = pd.read_csv('mental_health_workplace_survey.csv')

# Select features and target
X  = health_data[['WorkLifeBalanceScore', 'ManagerSupportScore', 'JobSatisfaction']]
y = health_data['StressLevel']  # Continuous target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Predict for sample input
sample_input = [[int(input_wlb), int(input_mss), int(input_js)]]
sample_predictions = model.predict(sample_input)
print("Predicted Stress Levels:", sample_predictions)

