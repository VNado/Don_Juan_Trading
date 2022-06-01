from ctypes.wintypes import PINT
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

#El carro de compras
@app.route('/carrito')
def carrito():
    #hacer consulta de productos en carrito respecto al id del cliente
    cur = mysql.connection.cursor()
    cur.execute("select nombre_prod, cantidad, precio, total, id_carro, id_producto from carrito_temp where id_cliente = "+str(session['user']))
    carrito = cur.fetchall()
    # si no hay productos en el carrito
    if len(carrito) == 0:
        mensages = "No hay productos en el carrito"
        return render_template('carrito.html', mensage=mensages)
    # sumar subtotales
    total = 0
    for i in range(len(carrito)):
        total += float(carrito[i][3])
    return render_template('carrito.html', registros=carrito, total=total)
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
@app.route('/carrito/eliminar/<string:id_carro>')
def eliminar_carrito(id_carro):
    cur = mysql.connection.cursor()
    cur.execute("delete from carrito_temp where id_carro = "+id_carro)
    mysql.connection.commit()
    return redirect(url_for('carrito'))
@app.route('/carrito/editar/<string:id_prod>')
def editar_carrito(id_prod):
    cur = mysql.connection.cursor()
    cur.execute("""SELECT carrito_temp.id_carro, carrito_temp.id_cliente, carrito_temp.id_producto,
        carrito_temp.nombre_prod, carrito_temp.cantidad, carrito_temp.precio,
        producto.descripcion_corta, producto.imagen FROM DonJuanTrading.carrito_temp, DonJuanTrading.producto
        WHERE id_prod ="""+ id_prod +";")
    registro = cur.fetchone()
    return render_template('editarcarro.html', registros=registro)
@app.route('/carrito/editar/editado', methods=['GET', 'POST'])
def editado_carrito():
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        id_prod = request.form['id_prod']
        id_carro = request.form['id_carro']
        precio = request.form['precio']
        precio = float(precio)
        total = precio * int(cantidad)
        cur = mysql.connection.cursor()
        cur.execute("update carrito_temp set cantidad = "+cantidad+", total = "+str(total)+" where id_carro = "+id_carro)
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

#Finalizar compra
@app.route('/finalizar_compra/registroEnvio', methods=['POST', 'GET'])
def registroEnvio():
    #sumar subtotales
    cur = mysql.connection.cursor()
    cur.execute("SELECT SUM(total) FROM carrito_temp")
    subtotal = cur.fetchone()
    subtotal = subtotal[0]
    return render_template('registroEnvio.html', totali=subtotal)
@app.route('/finalizar_compra/PagoFinalizado', methods=['POST', 'GET'])
def PagoFinalizado():
    #La base va a ser el carrito temporal
    #Obtneer cuantos productos tiene el cliente
    cur = mysql.connection.cursor()
    cur.execute("SELECT count(*) FROM carrito_temp WHERE id_cliente = "+str(session['user'])+";")
    cantidad = cur.fetchone()
    cantidad = cantidad[0]
    #Guardarlo en una varible comodin
    cantidad_productos = cantidad
    print(cantidad_productos)
    #Obtener solo la fecha actual
    now = datetime.now()
    fecha = now.date()
    print(fecha)
    #De la tabla de carrito_temp, obtener los id_producto, precio, cantidad, total del id_cliente
    cur.execute("SELECT id_producto, precio, cantidad, total FROM carrito_temp WHERE id_cliente = "+str(session['user'])+";")
    productos = cur.fetchall()
    #Guardarlos en un arrelgo
    informacion_productos = []
    for producto in productos:
        informacion_productos.append(producto)
    i = 0
    while cantidad_productos > i:
        print(informacion_productos[i])
        i = i + 1
    #insertar los datos a la tabla ventas_realizadas
    i = 0
    while cantidad_productos > i:
        cur.execute("""INSERT INTO ventas_realizadas(id_prod, id_cliente, fecha_venta, cantidad_de_producto, total_de_venta, estado_de_venta) 
        VALUES (%s, %s, %s, %s, %s, %s)""", (informacion_productos[i][0], session['user'], fecha, informacion_productos[i][2], informacion_productos[i][3], 'Enviado'))
        mysql.connection.commit()
        i = i + 1
    #Alterar la tabla producto, restando las existencias de los productos comprados
    i = 0
    while cantidad_productos > i:
        cur.execute("""UPDATE producto SET existencias = existencias - %s WHERE id_prod = %s""", (informacion_productos[i][2], informacion_productos[i][0]))
        mysql.connection.commit()
        i = i + 1
    #Obtner los id_carro del id_cliente
    cur.execute("SELECT id_carro FROM carrito_temp WHERE id_cliente = "+str(session['user'])+";")
    id_carro = cur.fetchall()
    #Guardarlos en un arreglo
    id_carro_cliente = []
    for id_carros in id_carro:
        id_carro_cliente.append(id_carros)
    i = 0
    while cantidad_productos > i:
        print("ID_CARRO_CLIENTE" + str(id_carro_cliente[i]))
        i = i + 1
    #Borrar los registros de carrito_temp dependiendo del id_carro y id_cliente
    i = 0
    while cantidad_productos > i:
        cur.execute("DELETE FROM carrito_temp WHERE id_carro = "+str(id_carro_cliente[i][0])+" AND id_cliente = "+str(session['user'])+";")
        mysql.connection.commit()
        i = i + 1
    return render_template('listo.html', cliente=session['user'])

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
        descripcion_corta = request.form['descripcion_corta']
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
        cur.execute("INSERT INTO producto(nombre_prod, descripcion, precio, imagen, descripcion_corta) VALUES (%s, %s, %s, %s, %s)", (nombre_prod, descripcion, precio_compra, filename, descripcion_corta))
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

#ecuesta
@app.route('/Califiquenos')
def Califiquenos():
    return render_template('encuesta.html')
@app.route('/Califiquenos/finalizado', methods=['POST', 'GET'])
def Califiquenos2():
    return render_template('listo.html')
#pedidos
@app.route('/ver/pedidos/')
def ver_pedidos():
    #Ejeuta consulta para obtener los pedidos
    cur = mysql.connection.cursor()
    cur.execute("""SELECT producto.imagen, producto.nombre_prod, producto.precio, ventas_realizadas.cantidad_de_producto, ventas_realizadas.total_de_venta, ventas_realizadas.estado_de_venta FROM producto, ventas_realizadas
    WHERE producto.id_prod = ventas_realizadas.id_prod AND ventas_realizadas.id_cliente = %s;""", (str(session['user'])))
    data = cur.fetchall()
    #Ejecutar la siguiente consulta para obtener la direccion del cliente
    cur.execute("""SELECT concat_ws(' ', calle_num, colonia, c_p, ciudad) as Direccion FROM cliente WHERE id_cliente= %s;""", (str(session['user'])))
    data2 = cur.fetchone()
    return render_template('ver_pedidos.html', registros=data, registros2=data2)

##############################################################################################
#APP functions

############################################################################################

if __name__ == '__main__':
    app.run(debug=True)
