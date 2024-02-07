
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! </br> <p>This is a demo website running on Azure Web Service. Darren Testing beware! </p>'

if __name__ == '__main__':
    app.run(debug=True)
