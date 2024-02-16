from wtforms import Form
from wtforms import StringField, TextAreaField,SelectField,RadioField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    nombre=StringField('nombre', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=10, message='ingresa nombre valido')
        
    ])
    apaterno=StringField('apaterno')
    amaterno=StringField('amaterno')
    
    edad=IntegerField('edad',
        [validators.number_range(min=1, max=20, message='valor no valido')]              ) 
   # materias=SelectField(choices=[('Español','esp'),('Matematicas','mat'), ('Ingles','ING') ])
    email=EmailField('email',[
        validators.Email(message='Ingrese un correo valido')
    ])
    #radios=RadioField('Curso',choices=[('1','1'),('2','2'),('3','3')])