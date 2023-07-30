from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo! desde debug mode"

if __name__=='__main__':
    app.run(debug=True)#, port=500)
