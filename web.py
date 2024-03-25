from flask import Flask, request, render_template
from joblib import load

app = Flask(__name__)
model = load('decision_tree_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    sqfeet = float(request.form['sqfeet'])
    # Perform prediction using the loaded model
    prediction = model.predict([[bedrooms, bathrooms, sqfeet]])
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)