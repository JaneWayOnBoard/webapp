# webapp
Build a Python Web Server with Flask
PI PROJECT : web server + simple web site 

You’ll set up a web server and create a simple website using Flask, Python, and HTML/CSS.

"""Install python3"""
sudo apt update
sudo apt install python3 idle3

"""install package/library/module : flask"""
sudo pip3 install name_of_m


"""Open a terminal or command prompt window, and make a new directory called webapp for your project."""
mkdir webapp

"""Use the change directory command cd to open the new directory."""
cd webapp

"""Create a new file by clicking File and then New file, and save it as app.py inside the webapp folder you just created."""


"""Now enter the following lines of code into the blank app.py window:"""

from flask import Flask

app = Flask(__name__)

"""determines the entry point; the / means the root of the website, so http://127.0.0.1:5000/"
@app.route('/') 
"""the name you give to the route; this one is called index, because it’s the index (or home page) of the website"""
def index():
"""content of the web page, which is returned when the user goes to this URL"""
    return 'Hello world'

"""Add a new page : create a new route by adding these lines of code below the first route: """
@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


"""Enter the command python3 app.py into the terminal window."""

"""If everything has been set up correctly, you should see an output similar to this:

* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger pin code: ***-***-***
"""

"""Open your web browser and enter the URL http://127.0.0.1:5000/. 
You should see a white screen with the words Hello world.
Note: 127.0.0.1 means ‘home’, i.e. this computer. :5000 means ‘port 5000’, 
which is the port the web server is running on.
"""

USE HTML

"""First, create a templates directory in your webapp directory by entering 
this into the terminal or command prompt window: """
mkdir templates

"""Create a new file in IDLE by clicking File and New File, and save this file as index.html 
in your templates folder. Enter the following HTML code in index.html:
"""

<html>
<body>
<h1>My website</h1>
</body>
</html>


ADD CSS

"""First, return to the terminal/command prompt window and navigate to the webapp directory. 
If you’re in the templates directory, go back up one level with cd ...
Create a new directory called static.
"""
mkdir static

"""Create a new file in IDLE by clicking File and New File, and save this file as style.css 
in the static folder you just created.


Add the following CSS rules to the file:

body {
    background: red;
    color: yellow;
}
"""

LEARN MORE ABOUT WEB DEVELOPPEMENT
https://developer.mozilla.org/en-US/docs/Learn

ABOUT FLASK
http://flask.pocoo.org/docs/1.0/
