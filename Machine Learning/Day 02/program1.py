# Import required packages
import numpy as np
import pickle

# Load the model from the pickle file
with open('./model.pkl', 'rb') as file:
    model = pickle.load(file)

# Get the SAT Score from the user
sat_score = float(input("Enter the SAT score: "))

# Inference the model
gpa = model.predict([[sat_score]])
print(f"Your GPA Will be : {gpa[0]:.2f}")