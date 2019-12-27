# import flask dependencies
from flask import Flask, request, make_response, jsonify

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'DevOps'

@app.route('/integrantes')
def integrantes():
    return jsonify(['Flavio - 333565', 'Pedro - 334109', 'Rafael - 333829', 'Rodrigo - 333241', 'Wellington - 333878'])

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    # fetch action from json
    action = req.get('queryResult').get('action')

    # return a fulfillment response
    return {'fulfillmentText': 'This is a response from webhook.'}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
