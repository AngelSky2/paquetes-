from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Paquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.String(50), nullable=False)

    movimientos = db.relationship('Movimiento', backref='paquete', lazy=True)

    def __repr__(self):
        return f'<Paquete {self.nombre}>'

class Movimiento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.DateTime, nullable=False)
    estado_actual = db.Column(db.String(50), nullable=False)


    paquete_id = db.Column(db.Integer, db.ForeignKey('paquete.id'), nullable=False)

    def __repr__(self):
        return f'<Movimiento {self.estado_actual}>'
