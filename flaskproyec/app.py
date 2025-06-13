from flask import Flask 

app = Flask(__name__)

#ruta simple
@app.route('/')
def home():
    return 'hola mundo FLASK'

#ruta con parametros 
@app.route('/saludo/<nombre>')
def saludar(nombre):
    return 'Hola,'+nombre+'!!!'

#Ruta try -cath 
app.errorhandler(404)
def paginaNoEncontrada(e):
    return 'cuidado error de capa 8!',404

#ruta double 
@app.route('/usuario')
@app.route('/usuario')
def dobleroute():
    return 'soy el mismo recurso del servidor'

#ruta POST 
@app.route("/formulario", methods = ["POST"])
def formulario():
    return "soy un formulario"



if __name__ == '__main__':
    app.run(port=3000,debug=True)