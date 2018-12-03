from flask import Flask, render_template

app = Flask(__name__)

"""In the ‘Hello Love’ example, we used a single route:"""
@app.route('/')
def index():
    return render_template('index.html')

"""Setting a new route for a new page"""
@app.route('/darling')
def darling():
    return render_template('darling.html')

@app.route('/hello/<darling>')
def hello(darling):
    return render_template('page.html', darling=darling)


"""To run the web server and your app:"""
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

"""Note: the host='0.0.0.0' means the web app will be accessible to any device on the network.
Open your web browser and enter the URL http://127.0.0.1:5000/. 
You should see a white screen with the words Hello Love
127.0.0.1 means ‘home’, i.e. this computer.
:5000 means ‘port 5000’, which is the port the web server is running on.
"""
