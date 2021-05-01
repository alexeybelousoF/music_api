import flask
from flask import request, jsonify
from music_parser import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# serch route
@app.route('/api/v1/music/search/', methods=['GET'])
def search_route():
  if 'query' in request.args:
    query = request.args['query']
    offset = int(request.args['offset']) or 0
    result = search(query, offset)
    return result
  else:
    return "Error: No query field provided. Please specify an query."

# popular route
@app.route('/api/v1/music/popular/', methods=['GET'])
def popular_route():
  if 'offset' in request.args:
    offset = int(request.args['offset']) or 0
    result = popular(offset)
    return result

# newsest route
@app.route('/api/v1/music/newsest/', methods=['GET'])
def newsest_route():
  if 'offset' in request.args:
    offset = int(request.args['offset']) or 0
    result = newsest(offset)
    return result

@app.route('/api/v1/music/user/', methods=['GET'])
def user_route():
  if 'user_id' in request.args:
    user_id = int(request.args['user_id']) or 0
    result = user_(user_id)
    return result
  else:
    return "Error: No user_id field provided. Please specify an user_id."

app.run()