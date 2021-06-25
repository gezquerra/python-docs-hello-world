from flask import Flask, request, jsonify
from urllib.parse import unquote_plus
import json
import re


app = Flask(__name__)

evalart_customer_config = {
  "config": {
    "fields": [
      {
        "id": "persona",
        "label": "Persona",
        "placeholder": "Select persona",
        "type": "select",
        "options": [
          { "id": 1, "label": "Senior developer" },
          { "id": 2, "label": "Junior developer" }
        ]
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

    #url = 'https://smart.requestcatcher.com/test'
#
    #headers = {"Content-Type": "application/json"}
    #x = requests.post(url, data = payload,headers = headers)
    #print (x)
    return ("", 200, None)


#app.run()

