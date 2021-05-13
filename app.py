from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/data')
def helloData():
    return jsonify({"name":"adam","email":"adam@gmail.com"})

if __name__ == '__main__':
    app.run(port=5001,host="0.0.0.0",debug=False)
