from flask import Flask, request, render_template, Response
from flask_wtf.csrf import CSRFProtect
from flask import g

#Cuando pasemos la validación de los datos, no deja avanzar si tiene validación CSRFProject
from flask import flash
import forms

app = Flask(__name__)
#Protección de formularios 19/02/2024
app.secret_key = 'esta es la clave secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.prueba='hola'
    print('antes 1')

@app.route("/")
def hola():
    return "<p>Hola mundo<p>"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    print('dentro 2')
    valor=g.prueba
    print('el dato es: {}'.format(valor))
    nom = ''
    email = ''
    alum_form = forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        print('hola')
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data
        email = alum_form.email.data
        mensaje = 'Bienvenido: {}'.format(nom) 
        flash(mensaje)
        print("nombre:{}".format(nom))
        print("apaterno:{}".format(apa))
        print("amaterno:{}".format(ama))
        print("correo: {}".format(email)) 

    return render_template("alumnos.html", form=alum_form, nom=nom, email=email)

@app.after_request
def after_request(response):
    print('después de ruta 3')
    return response

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/hola")
def func():
    return "<p>Saludo desde hola<p>"

@app.route("/saludo")
def func1():
    return "<p>Saludo desde saludo con alguna de los decoradores<p>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<p><p>" + nom

@app.route("/numero/<int:n1>")
def numero(n1):
    return "<p>El valor es {}<p>".format(n1)

@app.route("/varios/<string:nom>/<int:id>")
def cadena(nom, id):
    return "ID {} NOMBRE {}".format(id, nom)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma de {} + {} = {}".format(n1, n2, n1 + n2)

@app.route("/multiplica", methods=["GET", "POST"])
def mult():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1>el resultado es: {} </h1>".format(str(int(num1) * int(num2)))
    else:
        return '''
            <form action="/multiplica" method="POST">
            <label>N1: </label>
            <input type="text" name="n1">
            <label>N2: </label>
            <input type="text" name="n2">
            <input type="submit">
            </form>
        '''

@app.route("/formulario1", methods=["GET", "POST"])
def calculo():
    return render_template("formulario1.html")

@app.route("/resultado", methods=["GET", "POST"])
def mult1():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1>El resultado es: {} </h1>".format(str(int(num1) * int(num2)))

if __name__ == "__main__":
    app.run(debug=True)
