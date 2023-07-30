from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # return "Hola mundo! desde debug mode"
    data = {
        'tab_title':'Titulo de la pagina web',
        'title': 'Este es el titulo de mi pagina web'
    }
    # data es un diccionario con parametros para usar la plantilla de forma dinámica
    return render_template('index.html', data)

if __name__=='__main__':
    app.run(debug=True)#, port=500)
