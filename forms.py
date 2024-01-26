from wtforms import format
from wtforms import StringField, TextAreaField, SelectField,RadioField
from wtforms import EmailField


class UserForm(Form):
    nombre=StringField("nombre")
    email=EmailField("email")
    apaterno=TextAreaField("apaterno")
    materias=SelectField(choices=[('Español', 'Esp',),('Mat', 'Matematicas'),
                                  ('Ingles', 'ING')])
    radios=RadioField('Curso', choices=[("1", "1"),("2", "2"),("3", "3")])