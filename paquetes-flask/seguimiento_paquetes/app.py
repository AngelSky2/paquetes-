from flask import Flask, render_template, request, redirect, url_for
from models import db, Paquete, Movimiento
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///paquetes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    paquetes = Paquete.query.all()
    for paquete in paquetes:
        ultimo_movimiento = Movimiento.query.filter_by(paquete_id=paquete.id).order_by(Movimiento.fecha.desc()).first()
        paquete.ultimo_movimiento = ultimo_movimiento  
    return render_template('index.html', paquetes=paquetes)

@app.route('/nuevo_paquete', methods=['GET', 'POST'])
def nuevo_paquete():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        estado = 'En tránsito'
        paquete = Paquete(nombre=nombre, direccion=direccion, estado=estado)
        db.session.add(paquete)
        db.session.commit()

        movimiento = Movimiento(
            fecha=datetime.now(),
            estado_actual=estado,
            paquete_id=paquete.id
        )
        db.session.add(movimiento)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('nuevo_paquete.html')

@app.route('/actualizar_estado/<int:id>', methods=['GET', 'POST'])
def actualizar_estado(id):
    paquete = Paquete.query.get(id)
    if request.method == 'POST':
        nuevo_estado = request.form['estado']
        paquete.estado = nuevo_estado
        db.session.commit()

        movimiento = Movimiento(
            fecha=datetime.now(),
            estado_actual=nuevo_estado,
            paquete_id=paquete.id
        )
        db.session.add(movimiento)
        db.session.commit()
        
        return redirect(url_for('index'))

    return render_template('actualizar_estado.html', paquete=paquete)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
