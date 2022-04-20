import flask
from flask import request, jsonify

#====== import the path of twitter methods =====#
import sys
sys.path.append("./twitter")
#################################################

# api methods import
from user_search import search_users
from tweet_search import search_tweets

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>OSINT Project API Home Page!</h1><p>Copyrights @2022 TDHCHDK</p>"

# A route to return user search results
@app.route('/api/v1/twitter_search/', methods=['GET'])
def search_twitter_users():
    # Check if a `query`` was provided as part of the URL.
    # If `query` is provided, assign it to a variable.
    # If not, display an error in the browser.
    if 'q' in request.args:
        q = request.args['q']
    else:
        return "Error: No query provided for search. Please specify a query `q` as a param."
    
    if 'f' in request.args:
        f = request.args['f']
    else:
        return "Error: No search type provided. Please specify a search type `f` as a param."

    # Call twitter user search method and get results
    results = []
    if f == "user":
        results = search_users(q)
    elif f == 'tweet':
        results = search_tweets(q)
    else:
        return f"Error: Search type `{f}` does not exist. Please specify a supported search type (tweet, user)."

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()