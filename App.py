import email
from fileinput import filename
import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from mysqlx import Row
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)
# MySQL configurations
app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''
mysql = MySQL(app)
# App configurations
app.secret_key = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = 'static/img'
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

#entities#
from models.entities.user import User


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
    #consultar productos
    cur = mysql.connection.cursor()
    cur.execute("select * from producto")
    prod = cur.fetchall()
    return render_template('tienda.html', productos=prod)

@app.route('/carrito')
def carrito():
    #hacer consulta de productos en carrito respecto al id del cliente
    cur = mysql.connection.cursor()
    cur.execute("select nombre_prod, cantidad, precio, total from carrito_temp where id_cliente = "+str(session['user']))
    carrito = cur.fetchall()
    # si no hay productos en el carrito
    if len(carrito) == 0:
        mensages = "No hay productos en el carrito"
        return render_template('carrito.html', mensage=mensages)
    return render_template('carrito.html', registros=carrito, mensaje='')
@app.route('/carrito/agregar', methods=['GET', 'POST'])
def agregar_carrito():
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        id_prod = request.form['id_prod']
        cur = mysql.connection.cursor()
        cur.execute("select nombre_prod, precio from producto where id_prod = "+id_prod)
        precio = cur.fetchone()
        nombre_prod = precio[0]
        precio = precio[1]
        precio = float(precio)
        total = precio * int(cantidad)
        cur.execute("insert into carrito_temp (id_cliente, id_producto, nombre_prod, cantidad, precio, total) values ("+str(session['user'])+", "+id_prod+", '"+nombre_prod+"', "+cantidad+", "+str(precio)+", "+str(total)+")")
        mysql.connection.commit()
        return redirect(url_for('carrito'))
    else:
        return redirect(url_for('carrito'))

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
@app.route('/registro/paso2' , methods=['POST', 'GET'])
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
        contrasena2 = request.form['contrasena2']
        #verificar contraseñas
        if contrasena != contrasena2:
            flash('Las contraseñas no coinciden', 'danger')
            return redirect(url_for('registro1'))
        #Encriptacion de contrasena
        contrasena = generate_password_hash(contrasena)
        #verificar correo
        cur = mysql.connection.cursor()
        cur.execute("SELECT correo FROM cliente WHERE correo = %s", [correo])
        if cur.rowcount == 0:
            return render_template('registro2.html')
        else:
            flash('Correo ya registrado', 'danger')
            return redirect(url_for('registro1'))
    return render_template('registro2.html')
#@app.route('/registro/paso3')
#def registro3():
    #return render_template('registro3.html')
@app.route('/registro/finalizado', methods=['POST', 'GET'])
def registro4():
    if request.method == 'POST':
        #Extraccion de datos
        global nombre 
        global apellido
        global correo
        global contrasena

        global calle_num
        global colonia
        global c_p
        global ciudad
        global telefono

        now = datetime.now()

        calle_num = request.form['calle_num']
        colonia = request.form['colonia']
        c_p = request.form['c_p']
        ciudad = request.form['ciudad']
        telefono = request.form['telefono']

        #verificar c_p
        if len(c_p) < 5 and len(c_p) > 5:
            flash('Codigo postal invalido', 'danger')
            return redirect(url_for('registro2'))
        #verificar telefono
        if len(telefono) != 10:
            flash('Telefono invalido', 'danger')
            return redirect(url_for('registro2'))

        #se insertan los datos en la base de datos
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cliente(nombre, apellido, correo, contrasena, calle_num, colonia, c_p, ciudad, telefono, antiguedad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (nombre, apellido, correo, contrasena, calle_num, colonia, c_p, ciudad, telefono, now.date()))
        mysql.connection.commit()
        #se avisa que se registro correctamente
        #flash('Registro exitoso!')
    session.pop('_flashes', None)
    return render_template('registro4.html')
#Fin de registro

@app.route('/sangre_indio')
def producto1():
    #consulta para informacion del producto
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM producto WHERE id_prod = 1;")
    data = cur.fetchone()
    return render_template('producto1.html', registros=data)

@app.route('/fantasma')
def producto2():
    #consulta para informacion del producto
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM producto WHERE id_prod = 2;")
    data = cur.fetchone()
    return render_template('producto2.html', registros=data)

@app.route('/plata')
def producto3():
    #consulta para informacion del producto
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM producto WHERE id_prod = 3;")
    data = cur.fetchone()
    return render_template('producto3.html', registros=data)


@app.route('/crearproducto', methods=['POST', 'GET'])
def crearproducto():
    return render_template('crearproducto.html')
@app.route('/crearproducto/finalizado', methods=['POST', 'GET'])
def crearproducto2():
    if request.method == 'POST':
        #Extraccion de datos

        nombre_prod = request.form['nombre_prod']
        descripcion = request.form['descripcion']
        precio_compra = request.form['precio']
        f = request.files['imagen']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #verificar precio
        if precio_compra == "":
            flash('El precio de venta no puede ser menor al de compra', 'danger')
            return redirect(url_for('crearproducto'))
        #verificar nombre
        if nombre_prod == "":
            flash('El nombre no puede estar vacio', 'danger')
            return redirect(url_for('crearproducto'))
        #verificar descripcion
        if descripcion == "":
            flash('La descripcion no puede estar vacia', 'danger')
            return redirect(url_for('crearproducto'))
        #se insertan los datos en la base de datos
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO producto(nombre_prod, descripcion, precio, imagen) VALUES (%s, %s, %s, %s)", (nombre_prod, descripcion, precio_compra, filename))
        mysql.connection.commit()
        #se avisa que se registro correctamente
        flash('Producto creado exitosamente!', 'success')
        #limpiar flash
        session.pop('_flashes', None)
    #crear html
    ##User.crear_html()
    return render_template('listo.html')
@app.route('/producto/<string:prod>')
def producto(prod):
    #consulta para informacion del producto
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM producto WHERE nombre_prod = %s;", [prod])
    data = cur.fetchone()
    return render_template('template.html', registros=data)

##############################################################################################
#APP functions

############################################################################################

if __name__ == '__main__':
    app.run(debug=True)
