from flask import Flask,request,json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/success/<name>', methods=['GET'])
def success(name):
   return 'Welcome %s' % name

@app.route('/post/', methods=['POST'])
def post():
    if request.headers['Content-Type'] == 'application/json':
        return "Text Message: " + json.dumps(request.json)
    else:
        return "Invalid type"

if __name__ == '__main__':
    app.run(debug=True)

