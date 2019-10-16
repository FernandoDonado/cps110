# pylint: disable=E1135,E1136

from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    datestr = datetime.datetime.now()
    return f"""<html><body>Welcome!
    The time is {datestr}.
    <a href="/page2">Click here</a> for page 2.
    </body></html>"""

@app.route('/page2')
def page2():
    return """<html><body>Here is page 2.</body></html>"""

@app.route('/hello')
def hello():
    name = 'World'
    age = 15
    if 'name' in request.args:
        name = request.args['name']
    if 'age' in request.args:
        age = request.args['age']

    return f"""<html><body>
        <h1>Hello, {name}!</h1>
        You are {age} years old.</body></html>"""

# Launch the BottlePy dev server
if __name__ == "__main__":
    app.run(host='localhost', debug=True)

