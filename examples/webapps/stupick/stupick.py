from flask import Flask, send_from_directory
import os.path
import random
import glob

# To create a desktop shortcut using Chrome:
# "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --chrome-frame --app="http://sschaub.pythonanywhere.com/stupick"

app = Flask(__name__)
SOUNDS = [os.path.basename(x) for x in glob.glob("sounds/*")]

CUR_DIR = os.path.dirname(__file__)
students = []

@app.route('/stupick')
def picker():
    with open(os.path.join(CUR_DIR, 'stupick.html')) as htmlfile:
        HTML = htmlfile.read()

    student = random.choice(students)
    effect = random.choice(SOUNDS)

    return HTML.format(name=student[0], username=student[1], sound=effect)

@app.route('/<path:filename>')
def send_static(filename):
    """Serve up images and sounds."""
    return send_from_directory(CUR_DIR, filename)

if __name__ == '__main__':
    with open(os.path.join(CUR_DIR, 'cps110.txt')) as stufile: 
        for student in stufile:
            [_, _, firstname, lastname, username] = student.split(',')        
            students.append((firstname[0] + ". " + lastname, username))
    print("Loaded data: ", students)
    # Launch the Flask dev server
    app.run(host='localhost', debug=True)
