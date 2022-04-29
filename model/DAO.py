from _ast import In
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, BLOB, CHAR, Float, ForeignKey, Date
from flask_login import UserMixin
from sqlalchemy.orm import relationship
db = SQLAlchemy()
#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------catalogoMultas---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Login(UserMixin,db.Model):
    _tablename_ = 'login'
    id= Column(Integer, primary_key=True)
    login = Column(Integer, primary_key=True)
    password_hash = Column(String(20), nullable=False)

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

    def validar(self, correo, contrasena):
        login = None
        login = self.query.filter(Login.login == correo, Login. password_hash == contrasena,).first()
        return login

    def is_authenticated(self):
        return True


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

    def eliminacionLogica(self, id):
        obj = self.consultaIndividuall(id)
        db.estatus = '0'
        db.actualizar()
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

#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Proveedores---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

class Proveedores(db.Model):
        __tablename__ = 'proveedores'
        idProveedores = Column(Integer, primary_key=True)
        nombre = Column(String(45), nullable=False)
        direccion = Column(String(45), nullable=False)
        telefono = Column(CHAR(15), nullable=False)
        correo = Column(String(45), nullable=False)
        pais = Column(String(45), nullable=False)

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

        def eliminacionLogica(self, id):
            obj = self.consultaIndividuall(id)
            db.estatus = 'Inactiva'
            db.editar()


#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Editorial---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

class Editorial(db.Model):
    __tablename__ = 'editorial'
    idEditorial = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    direccion = Column(String(45), nullable=False)
    telefono = Column(CHAR(15), nullable=False)
    correo = Column(String(45), nullable=False)
    pais = Column(String(45), nullable=False)

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

    def eliminacionLogica(self, id):
        obj = self.consultaIndividuall(id)
        db.estatus = 'Inactiva'
        db.editar()



#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Libros---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
class Libros(db.Model):
    __tablename__ = 'libros'
    idLibros = Column(Integer, primary_key=True)
    idCategorias=Column(Integer, ForeignKey('categorias.idCategorias'))
    idEditorial=Column(Integer, ForeignKey('editorial.idEditorial'))
    titulo = Column(String(45), nullable=False)
    numEdicion = Column(Integer, nullable=False)
    numPaginas = Column(Integer, nullable=False)
    anioPublicacion= Column(Date, nullable=False)
    precioVenta= Column(Float, nullable=False)
    precioCompra= Column(Float, nullable=False)


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

    def eliminacionLogica(self, id):
        obj = self.consultaIndividuall(id)
        db.estatus = 'Inactiva'
        db.editar()

#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Libros Autor---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

class LibrosAutor(db.Model):
    __tablename__ = 'librosautor'
    idLibrosAutor = Column(Integer, primary_key=True)
    idLibros = Column(Integer, ForeignKey('libros.idLibros'))
    idAutor = Column(Integer, ForeignKey('autor.idAutor'))

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

    def eliminacionLogica(self, id):
        obj = self.consultaIndividuall(id)
        db.estatus = 'Inactiva'
        db.editar()


#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Autor---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------


class Autor(db.Model):
    __tablename__ = 'autor'
    idAutor = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    pais = Column(String(45), nullable=False)
    ciudad = Column(String(45), nullable=False)
    anioNacimiento = Column(Date, nullable=False)
    estudios = Column(String(45), nullable=False)



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

    def eliminacionLogica(self, id):
        obj = self.consultaIndividuall(id)
        db.estatus = 'Inactiva'
        db.editar()



#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Prestamo solo el dao---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------





class Prestamo(db.Model):
    __tablename__ = 'prestamo'
    idPrestamo = Column(Integer, primary_key=True)
    idUsuarios=Column(Integer, ForeignKey('usuarios.idUsuarios'))
    idBibliotecario=Column(Integer, ForeignKey('bibliotecario.idBibliotecario'))
    fechaprestamo = Column(Date, nullable=False)
    fechadevolucion = Column(Date, nullable=False)
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

    def eliminacionLogica(self, id):
        obj = self.consultaIndividuall(id)
        db.estatus = 'Inactiva'
        db.editar()





#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Multas Prestamo---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------





class MultasPrestamo(db.Model):
    __tablename__ = 'multasprestamo'
    idMultasPrestamo = Column(Integer, primary_key=True)
    idCatalogoMultas=Column(Integer, ForeignKey('catalogo.idCatalogoMultas'))
    idPrestamo=Column(Integer, ForeignKey('prestamo.idPrestamo'))
    cantPagar= Column(Float, nullable=False)
    fecha = Column(Date, nullable=False)


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

    def eliminacionLogica(self, id):
        obj = self.consultaIndividuall(id)
        db.estatus = 'Inactiva'
        db.editar()

#-----------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------Membresias---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

class Membresias(db.Model):
    __tablename__ = 'membresias'
    idMembresias = Column(Integer, primary_key=True)
    nombre = Column(String(45), nullable=False)
    precio = Column(Float, nullable=False)
    duracion = Column(Integer, nullable=False)
    cantidadLibros = Column(Integer, nullable=False)
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
#------------------------------------------------------Usuarios---------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    idUsuarios = Column(Integer, primary_key=True)
    nodedocumento = Column(Integer, nullable=False)
    nombreCompleto = Column(String(45), nullable=False)
    appaterno = Column(String(45), nullable=False)
    apmaterno = Column(String(45), nullable=False)
    sexo = Column(String(4), nullable=False)
    direccion = Column(String(45), nullable=False)
    telefono = Column(CHAR(15), nullable=False)
    email = Column(String(45), nullable=False)

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