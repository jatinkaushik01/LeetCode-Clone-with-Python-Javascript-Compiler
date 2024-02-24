# app.py

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Node.js service URL
nodejs_url = "http://nodejs-service:8080/submit_js_code"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_js_code', methods=['POST'])
def submit_js_code():
    try:
        js_code = request.form['js_code']

        # Send a POST request to the Node.js service
        response = requests.post(nodejs_url, data={'js_code': js_code})

        if response.status_code == 200:
            result = response.json()
            return render_template('result.html', result=result)
        else:
            return f"Error: {response.text}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
