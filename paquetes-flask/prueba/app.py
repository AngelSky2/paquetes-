from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'  # Cambia esto si tu DB no está en localhost
app.config['MYSQL_USER'] = 'root'       # Usuario de la base de datos
app.config['MYSQL_PASSWORD'] = ''       # Contraseña de la base de datos
app.config['MYSQL_DB'] = 'paquetesbd'   # Nombre de la base de datos

# Inicializar MySQL
mysql = MySQL(app)

# Ruta principal para ver todos los paquetes
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM paquetes")
    paquetes = cursor.fetchall()
    cursor.close()
    return render_template('index.html', paquetes=paquetes)

# Ruta para agregar un nuevo paquete
@app.route('/agregar_paquete', methods=['GET', 'POST'])
def agregar_paquete():
    cursor = mysql.connection.cursor()

    if request.method == 'POST':
        descripcion = request.form['descripcion']
        cliente_id = request.form['cliente_id']
        estado_id = request.form['estado_id']

        # Insertar el nuevo paquete
        cursor.execute("INSERT INTO paquetes (descripcion, cliente_id, estado_id) VALUES (%s, %s, %s)",
                       (descripcion, cliente_id, estado_id))
        mysql.connection.commit()  # Confirmar la transacción

        return redirect(url_for('index'))

    # Obtener la lista de clientes y estados para los formularios desplegables
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    cursor.execute("SELECT * FROM estadospaquete")
    estados = cursor.fetchall()

    cursor.close()
    return render_template('agregar_paquete.html', clientes=clientes, estados=estados)

# Ruta para editar un paquete
@app.route('/editar_paquete/<int:id>', methods=['GET', 'POST'])
def editar_paquete(id):
    cursor = mysql.connection.cursor()

    if request.method == 'POST':
        descripcion = request.form['descripcion']
        cliente_id = request.form['cliente_id']
        estado_id = request.form['estado_id']

        # Actualizar la información del paquete
        cursor.execute("UPDATE paquetes SET descripcion = %s, cliente_id = %s, estado_id = %s WHERE id = %s",
                       (descripcion, cliente_id, estado_id, id))
        mysql.connection.commit()

        return redirect(url_for('index'))

    # Obtener los datos del paquete que se va a editar
    cursor.execute("SELECT * FROM paquetes WHERE id = %s", (id,))
    paquete = cursor.fetchone()

    # Obtener los datos de clientes y estados
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    cursor.execute("SELECT * FROM estadospaquete")
    estados = cursor.fetchall()

    cursor.close()
    return render_template('editar_paquete.html', paquete=paquete, clientes=clientes, estados=estados)

# Ruta para eliminar un paquete
@app.route('/eliminar_paquete/<int:id>')
def eliminar_paquete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM paquetes WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('index'))

# Ruta para ver el seguimiento de un paquete
@app.route('/seguimiento_paquete/<int:id>')
def seguimiento_paquete(id):
    cursor = mysql.connection.cursor()

    # Obtener la información del paquete
    cursor.execute("SELECT * FROM paquetes WHERE id = %s", (id,))
    paquete = cursor.fetchone()

    # Obtener el historial de movimientos del paquete
    cursor.execute("SELECT * FROM movimientospaquete WHERE paquete_id = %s ORDER BY fecha_movimiento", (id,))
    movimientos = cursor.fetchall()

    cursor.close()
    return render_template('seguimiento_paquete.html', paquete=paquete, movimientos=movimientos)

if __name__ == '__main__':
    app.run(debug=True)
