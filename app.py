from flask import Flask, request, jsonify
from urllib.parse import unquote_plus
import json
import re

app = Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

evalart_customer_config = [{
  "config": {
    "fields": [
      {
        "id": "type",
        "label": "Test",
        "placeholder": "Select test",
        "type": "select",
        "optgroups": [
          {
            "label": "Logical tests",
            "options": [
              { "id": 1, "label": "Algorithm test" },
              { "id": 2, "label": "Data structure test" }
            ]
          },
          {
            "label": "Programming tests",
            "options": [
              { "id": 3, "label": "Javascript test" },
              { "id": 4, "label": "Ruby test" }
            ]
          }
        ]
      },
      {
        "id": "persona",
        "label": "Persona",
        "placeholder": "Select persona",
        "type": "select",
        "options": [
          { "id": 1, "label": "Senior developer" },
          { "id": 2, "label": "Junior developer" }
        ]
      },
    ]
  }
}]

def parse_request(req):
    """
    Parses application/json request body data into a Python dictionary
    """
    payload = req.get_data()
    #payload = unquote_plus(payload)
    #payload = re.sub('payload=', '', payload)
    payload = json.loads(payload)

    return payload

@app.route("/")
def hello():
    return "Hello, Azure!"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# A route to return config
@app.route('/config', methods=['GET'])
def api_config():
    return jsonify(evalart_customer_config)

# A route to return config
@app.route('/webhook', methods=['PUT','POST'])
def api_webhook():
    payload = parse_request(request)
    print (payload)
    return ("", 200, None)


#app.run()

