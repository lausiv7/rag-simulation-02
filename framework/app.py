from flask import Flask, jsonify
import requests
from config import LLM_URL

app = Flask(__name__)

@app.route('/check_llm_status', methods=['GET'])
def check_llm_status():
    try:
        response = requests.get(f"{LLM_URL}/status")
        if response.status_code == 200:
            return jsonify({"status": "LLM is reachable"}), 200
        else:
            return jsonify({"status": "LLM is not reachable"}), 500
    except requests.exceptions.RequestException:
        return jsonify({"status": "LLM is not reachable"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
