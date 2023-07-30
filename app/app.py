from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # return "Hola mundo! desde debug mode"
    cursos = ['PHP','Python','JAVA','GO','Kotlin','SCALA','javascript']
    data = {
        'tab_title':'Titulo de la pagina web',
        'title': 'Este es el titulo de mi pagina web',
        'lista': cursos,
        'sizeLista': len(cursos)
    }
    # data es un diccionario con parametros para usar la plantilla de forma dinámica
    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data ={
        'titulo': 'contacto',
        'nombre':   nombre,
        'edad': edad
    }
    return render_template('contacto.html',data = data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "OK"

def pagina_no_encontrada(error):
    # utilizar cualquiera de las 2 lineas
    # return render_template('404.html'), 404
    return redirect(url_for('index'))

if __name__=='__main__':
    app.add_url_rule('/query_string', view_func=query_string) # utilizar en el navegador 127.0.0.1:5000/query_string?param1=Jose&param2=239
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)#, port=500)
