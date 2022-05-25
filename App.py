import email
from flask import Flask, render_template, request, redirect, url_for, flash, session
from mysqlx import Row
from werkzeug.security import generate_password_hash, check_password_hash
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
# App variables
nombre = ""
apellido = ""
correo = ""
contrasena = ""
calle_num = ""
colonia = ""
c_p = ""
ciudad = ""
telefono = ""


#APP ROUTES
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena_plana = request.form['contrasena']
        print(contrasena_plana)
        cur=mysql.connection.cursor()
        cur.execute("SELECT contrasena FROM cliente WHERE correo = %s", [correo])
        if cur.rowcount == 0:
            flash('Correo no registrado', 'danger')
            return redirect(url_for('index'))
        else:
            cur=mysql.connection.cursor()
            cur.execute("SELECT contrasena FROM cliente WHERE correo = %s", [correo])
            user = cur.fetchone()
            print(user[0])
            respuesta_contra = check_password_hash(user[0], contrasena_plana)
            if respuesta_contra == False:
                flash('Contraseña incorrecta', 'danger')
                return redirect(url_for('index'))
            else:
                cur = mysql.connection.cursor()
                cur.execute("select id_cliente from cliente where correo = '"+correo+"';")
                id_cliente = cur.fetchone()
                session['user'] = id_cliente[0]
                print(id_cliente[0])
                return redirect(url_for('index'))
    else:
        return render_template('index.html')
    

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
@app.route('/cerrar_sesion')
def cerrar_sesion():
    session.clear()
    return redirect(url_for('index'))

@app.route('/entrada/<string:ira>')
def entrada(ira):
    return render_template('entrada.html', ira=ira)

#REGISTRO
@app.route('/registro')
def registro1():
    return render_template('registro1.html')
@app.route('/registro/paso2' , methods=['POST'])
def registro2():
    if request.method == 'POST':
        #Extraccion de datos
        global nombre
        global apellido
        global correo
        global contrasena

        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contrasena = request.form['contrasena']
        #Encriptacion de contrasena
        contrasena = generate_password_hash(contrasena)
    return render_template('registro2.html')
#@app.route('/registro/paso3')
#def registro3():
    #return render_template('registro3.html')
@app.route('/registro/finalizado', methods=['POST'])
def registro4():
    if request.method == 'POST':
        #Extraccion de datos
        global nombre 
        global apellido
        global correo
        global contrasena

        calle_num = request.form['calle_num']
        colonia = request.form['colonia']
        c_p = request.form['c_p']
        ciudad = request.form['ciudad']
        telefono = request.form['telefono']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cliente(nombre, apellido, correo, contrasena, calle_num, colonia, c_p, ciudad, telefono) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (nombre, apellido, correo, contrasena, calle_num, colonia, c_p, ciudad, telefono))
        mysql.connection.commit()
        flash('Registro exitoso!')
    return render_template('registro4.html')
#Fin de registro

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