from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('model/delay_model.pkl')

# Encode categorical like training (manual map for simplicity)
airline_map = {'AA': 0, 'DL': 1, 'UA': 2, 'WN': 3}  # example
airport_map = {'ATL': 0, 'LAX': 1, 'ORD': 2, 'DFW': 3}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    input_data = pd.DataFrame({
        'MONTH': [int(data['month'])],
        'DAY': [int(data['day'])],
        'DAY_OF_WEEK': [int(data['day_of_week'])],
        'AIRLINE': [airline_map.get(data['airline'], 0)],
        'ORIGIN_AIRPORT': [airport_map.get(data['origin'], 0)],
        'DESTINATION_AIRPORT': [airport_map.get(data['dest'], 0)],
        'SCHEDULED_DEPARTURE': [int(data['scheduled_dep'])]
    })

    prediction = model.predict(input_data)[0]
    result = "Flight is likely to be DELAYED" if prediction == 1 else "Flight is ON TIME"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
