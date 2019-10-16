from flask import Flask, send_from_directory
import random
import traceback
import os.path

WIDTH=700
HEIGHT=700

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

app = Flask(__name__)

@app.route('/')
def welcome():  
    svgdata = []
    svgdata.append("<rect x='0' y='0' width='{}' height='{}' fill='black' />".format(WIDTH, HEIGHT))

    for x in range(0, WIDTH+1, 100):
        svgdata.append("<line x1='{0}' y1='0' x2='{0}' y2='{1}' stroke='green' />".format(x, HEIGHT))

    for y in range(0, HEIGHT+1, 100):
        svgdata.append("<line x1='0' y1='{0}' x2='{1}' y2='{0}' stroke='green' />".format(y, WIDTH))

    svgdata.append("<image x='{0}' y='{1}' xlink:href='images/{2}' width='50' height='50' />".format(20, 30, 'duck.png'))
    svgdata.append("<text x='{0}' y='{1}' font-family='Verdana' font-size='10' stroke='white'>{2}</text>".format(10, 20, 'Some text here'))
        
    svgstring = '\n'.join(svgdata)
    return HTML_PAGE.format(WIDTH, HEIGHT, svgstring)

@app.route('/<path:filename>')
def send_static(filename):
    """Serve up images and sounds."""
    return send_from_directory(os.path.join(dir_path), filename)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<body>
<svg width="{0}" height="{1}">
  {2}
</svg>
</body>
</html>
"""

if __name__ == '__main__':
    # Launch the Flask dev server
    app.run(host="localhost", port=8080, debug=True)
    
