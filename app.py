from flask import Flask, request, jsonify
from urllib.parse import unquote_plus
import json
import re


app = Flask(__name__)

evalart_customer_config = {
  "config": {
    "fields": [
      {
        "placeholder": "Selecciona un proceso de Evalart",
        "type": "select",
        "options": [
          {
            "id": "22438",
            "label": "Proceso de prueba THT"
          },
          {
            "id": "22447",
            "label": "Prueba DISC y Big 5"
          }
        ],
        "id": "process",
        "label": "Proceso"
      }
    ]
  }
}


@app.route("/")
def hello():
    return "Hello, Azure!"

# A route to return config
@app.route('/config', methods=['GET'])
def api_config():
    return jsonify(evalart_customer_config)

# A route to return config
@app.route('/webhook', methods=['PUT','POST'])
def api_webhook():
    import requests

    payload = request.get_data()
    print (payload)

    url = 'https://smart.requestcatcher.com/test'
    headers = {"Content-Type": "application/json"}
    x = requests.post(url, data = payload,headers = headers)
    print (x)
    return ("", 200, None)


#app.run()

