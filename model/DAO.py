from _ast import In
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, BLOB, CHAR, Float, ForeignKey, Date
from flask_login import UserMixin
from sqlalchemy.orm import relationship
db = SQLAlchemy()
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------catalogoMultas---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

class CatalogoMultas(db.Model):
    __tablename__ = 'catalogomultas'
    idCatalogoMultas = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    descripcion = Column(String(140), nullable=False)
    precio = Column(Float, nullable=False)
    estatus = Column(Integer, nullable=False)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Categorias---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

class Categorias(db.Model):
    __tablename__ = 'categorias'
    idCategorias = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    estatus = Column(Integer, nullable=False)

    def consultaGeneral(self):
        return self.query.all()

    def consultaIndividual(self, id):
        return self.query.get(id)

    def insertar(self):
        db.session.add(self)
        db.session.commit()

    def actualizar(self):
        db.session.merge(self)
        db.session.commit()

    def eliminar(self, id):
        obj = self.consultaIndividual(id)
        db.session.delete(obj)
        db.session.commit()