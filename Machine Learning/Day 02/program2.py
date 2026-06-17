import numpy as np
from flask import Flask, render_template, request
import pickle

# Load the model
with open('./model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create Flask app
app = Flask(__name__)

# Home page
@app.route('/')
def root():
    return render_template('index.html')

# Prediction page
@app.route('/predict', methods=['POST'])
def predict():
    # Get SAT score from form
    sat_score = float(request.form.get('sat_score'))

    # Predict GPA
    gpa = model.predict([[sat_score]])

    return f"Your GPA will be: {gpa[0]:.2f}"

# Run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)