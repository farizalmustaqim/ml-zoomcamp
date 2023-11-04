import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'random_forest.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('stroke')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict(X)
    churn = y_pred >= 0.5

    result = {
        'stroke_probability': float(y_pred),
        'stroke': bool(churn)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8000)