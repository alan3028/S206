from flask import Flask,jsonify
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="alandavid10"
app.config['MYSQL_DB']="dbflask"

mysql=MySQL(app)

#ruta para probar la coneccion a MYSQL
@app.route('/DBCheck')
def DB_check():
    try:
        cursor= mysql.connection.cursor()
        cursor.execute('Select 1')
        return jsonify({'status':'ok','message':'Conectado con exito '}),200
    except MySQLdb.MySQLError as e :
          return jsonify({'status':'error','message':str(e)}),500

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