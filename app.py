# app.py
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load your trained machine learning model using joblib
model = joblib.load('fraud_detection_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input data from the form
        v1 = float(request.form['v1'])
        v2 = float(request.form['v2'])
        # ... repeat for other v features and amount
        amount = float(request.form['amount'])

        # Create a pandas DataFrame with the user input
        user_data = pd.DataFrame({
            'V1': [v1],
            'V2': [v2],
            # ... repeat for other v features and amount
            'Amount': [amount]
        })

        # Use your trained model to make predictions
        prediction = model.predict(user_data)

        # Render a template with the prediction result
        return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)


