# pylint: disable=E1135,E1136

from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return HTML_FORM

@app.route('/hello')
def hello():
    username = 'World'
    age = 15
    if 'username' in request.args:
        username = request.args['username']
    if 'age' in request.args:
        age = request.args['age']

    if username == "" or age == "":
        return HTML_FORM

    return """<html><body>
        <h1>Hello, {0}!</h1>
        You are {1} years old.</body></html>""".format(
            username, age)

HTML_FORM = """

<form action="/hello">
    Enter your username: <input type="text" name="username" value="Hello"><br>
    Enter your age: <input type="text" name="age" value="18"><br>
    <input type="submit" value="Click here for a friendly greeting">
</form>
"""


# Launch the BottlePy dev server
if __name__ == "__main__":
    app.run(host='localhost', debug=True)

