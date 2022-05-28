from flask import Flask, request, jsonify
from utilities import predict_pipeline

app = Flask(__name__)

@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text provided'})
    
    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as error:
        result = jsonify({'error': str(error)})
    
    return result

if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5000)
