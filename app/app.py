from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
import pyodbc

from config import config, db

# Models
from models.ModelUsuarios import ModelUsuarios

#Entities:
from models.entities.usuario import usuario

app = Flask(__name__)
    
cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + \
    db['SQLSERVER_SERVER']+';DATABASE='+db['SQLSERVER_DATABASE']+';UID='+db['u']+';PWD=' + db['p']

conn = pyodbc.connect(cstr)
    # return conn
    # conn = connection()
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM dbo.p1_prueba")


@app.before_request
def before_request():
    print('antes de la petición...')


@app.after_request
def after_request(response):
    print('después de la petición...')
    return response


@app.route('/')
def index():
    # return "Hola mundo! desde debug mode"
    cursos = ['PHP', 'Python', 'JAVA', 'GO', 'Kotlin', 'SCALA', 'javascript']
    data = {
        'tab_title': 'Titulo de la pagina web',
        'title': 'Este es el titulo de mi pagina web',
        'lista': cursos,
        'sizeLista': len(cursos),
        'navbar': {
            'home': "{url_for('index')}",
            'features': "{url_for('index')}",
            'thisproject': "https://github.com/juanpa800/FlaskProject"
        }
    }
    # data es un diccionario con parametros para usar la plantilla de forma dinámica
    return render_template('index.html', data=data)

@app.route('/login', methods=['GET','POST'])
def login():
    data = {
            'tab_title': 'Login',
            'title': 'Formulario para logearse'
        }
    if request.method == 'POST':
        user = usuario(request.form['userInput'],request.form['password'])
        logged_user = ModelUsuarios.login(conn, user)

        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('index'))
            else:
                flash("Contraseña incorrecta... sospechoso")
                return render_template('login.html',data = data)
        else:
            flash("Usuario no encontrado :(")


        return render_template('login.html', data = data)
    else:
        data = {
            'tab_title': 'Login',
            'title': 'Formulario para logearse'
        }
        return render_template('login.html', data = data)

@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'contacto',
        'nombre':   nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)


def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "OK"


@app.route('/cursos')
def listar_cursos():
    data = {}
    try:
        cursor = conn.cursor()
        query = '''
            SELECT *
            FROM usuarios
        '''
        cursor.execute(query)
        cursos = cursor.fetchall()
        # Por alguna razón que desconozco no funciona cursos para la jsonización,
        # se debe transformar como se muestra a continuación
        results = [tuple(row) for row in cursos]
        print(cursos)
        print(results)
        data['cursos'] = dict(results) #cursos

        data['mensaje'] = 'Exito'

    except Exception as e:
        data['mensaje'] = 'Error...'
    return jsonify(data)


def pagina_no_encontrada(_):
    # utilizar cualquiera de las 2 lineas
    # return render_template('404.html'), 404
    return redirect(url_for('index'))


if __name__ == '__main__':
    # utilizar en el navegador 127.0.0.1:5000/query_string?param1=Jose&param2=239
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.config.from_object(config['development'])
    app.run()  # , port=500)
