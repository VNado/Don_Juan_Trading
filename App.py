import email
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
# MySQL configurations
app.config['MYSQL_HOST'] = 'proyecto001.cmu1nv4edpom.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '%QmhdHWs'
app.config['MYSQL_DB'] = 'DonJuanTrading'
mysql = MySQL(app)
# App configurations
app.secret_key = 'mysecretkey'

#APP ROUTES
@app.route('/')
def index():
    #cur = mysql.connection.cursor()
    #cur.execute("SELECT * FROM registro")
    #data = cur.fetchall()
    return render_template('index.html')#, registros=data#)

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/proceso')
def proceso():
    return render_template('blog.html')

@app.route('/tienda')
def tienda():
    return render_template('tienda.html')

@app.route('/carrito')
def carrito():
    cur = mysql.connection.cursor()
    cur.execute("select producto.imagen, producto.nombre_prod, inventario.precio_vent, pedido.fecha_env from producto, inventario, pedido where pedido.id_cliente ="+"1;")
    data = cur.fetchall()
    return render_template('carrito.html', registros=data)

@app.route('/iniciodesesion')
def iniciodesesion():
    return render_template('iniciodesesion.html')

@app.route('/entrada/<string:ira>')
def entrada(ira):
    return render_template('entrada.html', ira=ira)

@app.route('/registro')
def registro1():
    return render_template('registro1.html')
@app.route('/registro/paso2')
def registro2():
    return render_template('registro2.html')
@app.route('/registro/paso3')
def registro3():
    return render_template('registro3.html')
@app.route('/registro/finalizado')
def registro4():
    return render_template('registro4.html')

@app.route('/sangre_indio')
def producto1():
    return render_template('producto1.html')

@app.route('/fantasma')
def producto2():
    return render_template('producto2.html')

@app.route('/plata')
def producto3():
    return render_template('producto3.html')
##############################################################################################
#APP functions

############################################################################################

if __name__ == '__main__':
    app.run(debug=True)