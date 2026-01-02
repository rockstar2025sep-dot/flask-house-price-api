from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

# -----------------------
# WEB APP (Browser)
# -----------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    area = float(request.form['area'])
    prediction = model.predict([[area]])[0][0]

    return render_template(
        'index.html',
        prediction_text=f'Price of House will be Rs. {int(prediction)}'
    )

# -----------------------
# API (ANDROID / REACT NATIVE)
# -----------------------
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json()

    area = float(data['area'])
    prediction = model.predict([[area]])[0][0]

    return jsonify({
        "area_sq_ft": area,
        "predicted_price_rs": int(prediction)
    })

# -----------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
