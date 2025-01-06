from flask import Flask, request, jsonify
from flask_cors import CORS
from gemini import Gemini_Model


app = Flask(__name__)

CORS(app)


@app.route('/greet', methods=['POST'])
def greet():
    data = request.json
    name = data.get('name', 'Unknown')
    return jsonify(message=f"Hello, {name} from Python!")


@app.route('/api/data', methods = [ 'GET'])
def get_data():
    data = {
        "message": "Hello from Flask!",
        "status": "success",
        "items": ["item1", "item2", "item3"]}
    return jsonify(data) 

@app.route('/gemini', methods=['POST'])
def gemini():
    data = request.json
    geminiOutput = Gemini_Model.output(data)
    return jsonify(geminiOutput)


if __name__ == '__main__':
    app.run(port=5000)