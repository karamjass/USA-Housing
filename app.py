from flask import Flask, request, jsonify, render_template
from model.predictor import Predictor

app = Flask(__name__)
predictor = Predictor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    prediction = predictor.predict(data)
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)