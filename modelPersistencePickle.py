# Topic of the Day: Model Persistence (pickle)
#
# Explanation: You don't want to retrain your model every time a user visits your website. You train it once, save it to a file, and load it instantly.
#
# pickle or joblib: The standard way to save Python objects.

import joblib
from sklearn.linear_model import LinearRegression

# 1. Train once
model = LinearRegression()
X = [[1], [2], [3]] # Rooms
y = [100, 200, 300] # Price
model.fit(X, y)

# 2. Save to file
joblib.dump(model, 'house_model.pkl')
print("Model saved!")

# --- LATER (In your API) ---

# 3. Load from file
loaded_model = joblib.load('house_model.pkl')
prediction = loaded_model.predict([[4]])
print(f"Predicted price for 4 rooms: {prediction[0]}")