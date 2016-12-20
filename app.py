# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for, json
from nlp import *
# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/similarity', methods=['POST'])
def similarity():
    jsonObj = request.get_json()
    threshold = jsonObj.get('threshold')
    q1 = jsonObj.get('string1')
    q2 = jsonObj.get('string2')
    q2 = q2.split('%')
    result = basic_paraphrase_recognizer(q1, q2, threshold)
    return json.dumps(result)

@app.route('/clustering', methods=['POST'])
def clustering():
    jsonObj = request.get_json()
    matrix = jsonObj.get('matrix')
    students = jsonObj.get('students')
    votes = jsonObj.get('votes')
    result = full_prop(matrix, students, votes, 1)
    print(result)
    return json.dumps(result)

@app.route('/test', methods=['POST'])
def test():
    jsonObj = request.get_json()
    print(jsonObj)
    return json.dumps(jsonObj)

# Run the app :)
if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("8080")
  )
