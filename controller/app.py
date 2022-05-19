import datetime
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from flask_login import current_user,login_user,logout_user,login_manager,login_required,LoginManager
from model.DAO import db, CatalogoMultas, Categorias, Proveedores,Editorial,Membresias,Login,Libros,Autor,LibrosAutor,Prestamo,MultasPrestamo,Usuarios,Bibliotecario
app=Flask(__name__, template_folder='../view', static_folder='../static')
Bootstrap(app)

#---------------------Conexion -----------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://user_erpbiblioteca:Alejandro@localhost/erpbiblioteca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

#________________________________________________________________________________
#--------------------------------login1-----------------------------------------
#________________________________________________________________________________

@login_manager.user_loader
def load_user(id):
    return CatalogoMultas.query.get(int(id))

@app.route('/')
def login():
    return render_template('common/login.html')

@app.route('/login/iniciandoSesion', methods=['post'])
def iniciandoSesion():
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    logi = Login()
    logi = logi.validar(correo, contrasena)
    if logi!= None:
        login_user(logi)
        return render_template('common/index.html')
    else:
        return render_template('common/login.html')

#________________________________________________________________________________
#--------------------------------COMUNES-----------------------------------------
#________________________________________________________________________________
@app.route('/index')
#@login_required
def inicio():
    return render_template('common/index.html')

# ________________________________________________________________________________
# --------------------------------catalogoMultas----------------------------------
# ________________________________________________________________________________
@app.route('/catalogoMultas/consultarCatalogoMultas')
# @login_required
def consultarCatalogoMultas():
    catalogo = CatalogoMultas()
    return render_template('/catalogoMultas/consultar.html', catal=catalogo.consultaGeneral())


@app.route('/catalogoMultas/registrarCatalogoMultas')
# @login_required
def registrarCatalogoMultas():
    return render_template('/catalogoMultas/nuevo.html')


@app.route('/catalogoMultas/guardandoCatalogoMultas', methods=['post'])
# @login_required
def guardandoCatalogoMultas():
    catalogo = CatalogoMultas()
    catalogo.nombre = request.form['nombre']
    catalogo.descripcion = request.form['descripcion']
    catalogo.precio = request.form['precio']
    catalogo.estatus = request.form['estatus']
    catalogo.insertar()
    flash('Catalogo de Multas registrado exitosamente')
    return redirect(url_for('consultarCatalogoMultas'))


@app.route('/catalogoMultas/ver/<int:id>')
# @login_required
def editarCatalogoMultas(id):
    catalogo = CatalogoMultas()
    return render_template('/catalogoMultas/editar.html', catal=catalogo.consultaIndividual(id))


@app.route('/catalogoMultas/editandoCatalogoMultas', methods=['post'])
# @login_required
def editandoCatalogoMultas():
    try:
        catalogo = CatalogoMultas()
        catalogo.idCatalogoMultas = request.form['idCatalogoMultas']
        catalogo.nombre = request.form['nombre']
        catalogo.descripcion = request.form['descripcion']
        catalogo.precio = request.form['precio']
        catalogo.estatus = request.form['estatus']
        catalogo.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/catalogoMultas/consultar.html', catal=catalogo.consultaGeneral())


@app.route('/catalogoMultas/eliminarLogicaCatalogoMultas/<int:id>')
# @login_required
def eliminarLogicaCatalogoMultas(id):
    catalogo = CatalogoMultas()
    catalogo.eliminacionLogica(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarCatalogoMultas'))

@app.route('/catalogoMultas/eliminarCatalogoMultas/<int:id>')
# @login_required
def eliminarCatalogoMultas(id):
    catalogo = CatalogoMultas()
    catalogo.eliminar(id)
    flash('eliminacion')
    return redirect(url_for('consultarCatalogoMultas'))


#________________________________________________________________________________
#--------------------------------Categorias----------------------------------
#________________________________________________________________________________
@app.route('/categorias/consultarCategorias')
#@login_required
def consultarCategorias():
    categorias = Categorias()
    return render_template('/categorias/consultar.html', cate=categorias.consultaGeneral())


@app.route('/categorias/registrarCategorias')
#@login_required
def registrarCategorias():
    return render_template('/categorias/nuevo.html')

@app.route('/categorias/guardandoCategorias',methods=['post'])
#@login_required
def guardandoCategorias():
    categorias = Categorias()
    categorias.nombre = request.form['nombre']
    categorias.estatus = request.form['estatus']
    categorias.insertar()
    flash('Catalogo de categorias registrado exitosamente')
    return redirect(url_for('consultarCategorias'))

@app.route('/categorias/ver/<int:id>')
#@login_required
def editarCategorias(id):
    categorias = Categorias()
    return render_template('/categorias/editar.html', cate=categorias.consultaIndividual(id))

@app.route('/categorias/editandoCategorias',methods=['post'])
#@login_required
def editandoCategorias():
    try:
        categorias =Categorias()
        categorias.idCategorias = request.form['idCategorias']
        categorias.nombre = request.form['nombre']
        categorias.estatus = request.form['estatus']
        categorias.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/categorias/consultar.html', cate=categorias.consultaGeneral())

@app.route('/categorias/eliminarCategoria/<int:id>')
#@login_required
def eliminarCategoria(id):
    categorias = Categorias()
    categorias.eliminar(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarCategorias'))

#________________________________________________________________________________
#--------------------------------Proveedores----------------------------------
#________________________________________________________________________________

@app.route('/proveedores/consultarProveedores')
#@login_required
def consultarProveedores():
    proveedores=Proveedores()
    return render_template('/proveedores/consultar.html',prov=proveedores.consultaGeneral())

@app.route('/proveedores/registrarProveedores')
#@login_required
def registrarProveedores():
    return render_template('/proveedores/nuevo.html')

@app.route('/proveedores/guardandoProveedores',methods=['post'])
#@login_required
def guardandoProveedores():
    proveedores = Proveedores()
    proveedores.nombre = request.form['nombre']
    proveedores.direccion = request.form['direccion']
    proveedores.telefono = request.form['telefono']
    proveedores.correo = request.form['correo']
    proveedores.pais = request.form['pais']
    proveedores.insertar()
    flash('Proveedor registrado exitosamente')
    return redirect(url_for('consultarProveedores'))

@app.route('/proveedores/ver/<int:id>')
#@login_required
def editarProveedores(id):
    proveedores = Proveedores()
    return render_template('/proveedores/editar.html', prov=proveedores.consultaIndividual(id))

@app.route('/proveedores/editandoProveedores',methods=['post'])
#@login_required
def editandoProveedores():
    try:
        proveedores =Proveedores()
        proveedores.idProveedores = request.form['idProveedores']
        proveedores.nombre = request.form['nombre']
        proveedores.direccion = request.form['direccion']
        proveedores.telefono = request.form['telefono']
        proveedores.correo = request.form['correo']
        proveedores.pais = request.form['pais']
        proveedores.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/proveedores/consultar.html', prov=proveedores.consultaGeneral())

@app.route('/proveedores/eliminarProveedores/<int:id>')
#@login_required
def eliminarProveedores(id):
    proveedores = Proveedores()
    proveedores.eliminar(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarProveedores'))


#________________________________________________________________________________
#--------------------------------Editorial----------------------------------
#________________________________________________________________________________

@app.route('/editorial/consultarEditorial')
#@login_required
def consultarEditorial():
    editorial=Editorial()
    return render_template('/editorial/consultar.html',edit=editorial.consultaGeneral())

@app.route('/editorial/registrarEditorial')
#@login_required
def registrarEditorial():
    return render_template('/editorial/nuevo.html')

@app.route('/editorial/guardandoEditorial',methods=['post'])
#@login_required
def guardandoEditorial():
    editorial =Editorial()
    editorial.nombre = request.form['nombre']
    editorial.direccion = request.form['direccion']
    editorial.telefono = request.form['telefono']
    editorial.correo = request.form['correo']
    editorial.pais = request.form['pais']
    editorial.insertar()
    flash('Editorial registrado exitosamente')
    return redirect(url_for('consultarEditorial'))

@app.route('/editorial/ver/<int:id>')
#@login_required
def editarEditorial(id):
    editorial = Editorial()
    return render_template('/editorial/editar.html', edit=editorial.consultaIndividual(id))

@app.route('/editorial/editandoEditorial',methods=['post'])
#@login_required
def editandoEditorial():
    try:
        editorial = Editorial()
        editorial.idEditorial = request.form['idEditorial']
        editorial.nombre = request.form['nombre']
        editorial.direccion = request.form['direccion']
        editorial.telefono = request.form['telefono']
        editorial.correo = request.form['correo']
        editorial.pais = request.form['pais']
        editorial.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/editorial/consultar.html', edit=editorial.consultaGeneral())

@app.route('/editorial/eliminarEditorial/<int:id>')
#@login_required
def eliminarEditorial(id):
    editorial = Editorial()
    editorial.eliminar(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarEditorial'))



#________________________________________________________________________________
#--------------------------------Multas prestamo----------------------------------
#________________________________________________________________________________





#________________________________________________________________________________
#--------------------------------Libros----------------------------------
#________________________________________________________________________________

@app.route('/libros/consultarLibros')
#@login_required
def consultarLibros():
    libros=Libros()
    categorias=Categorias()
    editorial=Editorial()
    return render_template('/libros/consultar.html',lib=libros.consultaGeneral(),cat=categorias.consultaGeneral(),edit=editorial.consultaGeneral())

@app.route('/libros/registrarLibros')
# @login_required
def registrarLibros():
    categorias=Categorias()
    editorial=Editorial()
    return render_template('/libros/nuevo.html', cat=categorias.consultaGeneral(),edit=editorial.consultaGeneral())


@app.route('/libros/guardandoLibros', methods=['post'])
# @login_required
def guardandoLibros():
    libros = Libros()
    libros.idCategorias = request.form['idCategorias']
    libros.idEditorial = request.form['idEditorial']
    libros.titulo = request.form['titulo']
    libros.numEdicion=request.form['numEdicion']
    libros.numPaginas = request.form['numPaginas']
    libros.anioPublicacion = request.form['anioPublicacion']
    libros.precioVenta = request.form['precioVenta']
    libros.precioCompra = request.form['precioCompra']
    libros.insertar()
    flash('libro registrado exitosamente')
    return redirect(url_for('consultarLibros'))



@app.route('/libros/ver/<int:id>')
#@login_required
def editarLibros(id):
    libros = Libros()
    categorias = Categorias()
    editorial = Editorial()
    return render_template('/libros/editar.html', lib=libros.consultaIndividual(id),cat=categorias.consultaGeneral(),edit=editorial.consultaGeneral())


@app.route('/libros/editandoLibros', methods=['post'])
#@login_required
def editandoLibros():
    try:
        libros = Libros()
        categorias = Categorias()
        editorial = Editorial()
        libros.idLibros=request.form['idLibros']
        libros.idCategorias = request.form['idCategorias']
        libros.idEditorial = request.form['idEditorial']
        libros.titulo = request.form['titulo']
        libros.numEdicion = request.form['numEdicion']
        libros.numPaginas = request.form['numPaginas']
        libros.anioPublicacion = request.form['anioPublicacion']
        libros.precioVenta = request.form['precioVenta']
        libros.precioCompra = request.form['precioCompra']
        libros.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/libros/consultar.html', lib=libros.consultaGeneral(),cat=categorias.consultaGeneral(),edit=editorial.consultaGeneral())

@app.route('/libros/eliminarLibros/<int:id>')
#@login_required
def eliminarLibros(id):
    libros = Libros()
    libros.eliminar(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarLibros'))

# ________________________________________________________________________________
# --------------------------------LIBROS autor-------------------------------------
# ________________________________________________________________________________



@app.route('/librosautor/consultarLibrosAutor')
#@login_required
def consultarLibrosAutor():
    librosautor=LibrosAutor()
    libros=Libros()
    autor=Autor()
    return render_template('/librosautor/consultar.html',libr=librosautor.consultaGeneral(),lib=libros.consultaGeneral(),aut=autor.consultaGeneral())

@app.route('/librosautor/registrarLibrosAutor')
# @login_required
def registrarLibrosAutor():
    libros = Libros()
    autor = Autor()
    return render_template('/librosautor/nuevo.html', lib=libros.consultaGeneral(),aut=autor.consultaGeneral())


@app.route('/librosautor/guardandoLibrosAutor', methods=['post'])
# @login_required
def guardandoLibrosAutor():
    librosautor = LibrosAutor()
    librosautor.idLibros= request.form['idLibros']
    librosautor.idAutor = request.form['idAutor']
    librosautor.insertar()
    flash('libro registrado exitosamente')
    return redirect(url_for('consultarLibrosAutor'))






@app.route('/librosautor/ver/<int:id>')
#@login_required
def editarLibrosAutor(id):
    librosautor = LibrosAutor()
    libros = Libros()
    autor = Autor()
    return render_template('/librosautor/editar.html', libr=librosautor.consultaIndividual(id),lib=libros.consultaGeneral(),aut=autor.consultaGeneral())


@app.route('/librosautor/editandoLibrosAutor', methods=['post'])
#@login_required
def editandoLibrosAutor():
    try:
        librosautor = LibrosAutor()
        libros = Libros()
        autor = Autor()
        librosautor.idLibrosAutor = request.form['idLibrosAutor']
        librosautor.idLibros = request.form['idLibros']
        librosautor.idAutor = request.form['idAutor']
        librosautor.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/librosautor/consultar.html', libr=librosautor.consultaGeneral(),lib=libros.consultaGeneral(),aut=autor.consultaGeneral())

@app.route('/librosautor/eliminarLibrosAutor/<int:id>')
#@login_required
def eliminarLibrosAutor(id):
    librosautor = LibrosAutor()
    librosautor.eliminar(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarLibrosAutor'))






# ________________________________________________________________________________
# --------------------------------MULTAS PRESTAMO-------------------------------------
# ________________________________________________________________________________



@app.route('/multasprestamo/consultarMultasPrestamo')
#@login_required
def consultarMultasPrestamo():
    multasprestamo=MultasPrestamo()
    catalogo=CatalogoMultas()
    prestamo=Prestamo()
    return render_template('/multasprestamo/consultar.html',mult=multasprestamo.consultaGeneral(),cat=catalogo.consultaGeneral(),pre=prestamo.consultaGeneral())

@app.route('/multasprestamo/registrarMultasPrestamo')
# @login_required
def registrarMultasPrestamo():
    catalogo = CatalogoMultas()
    prestamo = Prestamo()
    return render_template('/multasprestamo/nuevo.html',cat=catalogo.consultaGeneral(),pre=prestamo.consultaGeneral())


@app.route('/multasprestamo/guardandoMultasPrestamo', methods=['post'])
# @login_required
def guardandoMultasPrestamo():
    multasprestamo=MultasPrestamo()
    multasprestamo.idCatalogoMultas=request.form['idCatalogoMultas']
    multasprestamo.idPrestamo = request.form['idPrestamo']
    multasprestamo.cantPagar = request.form['cantPagar']
    multasprestamo.fecha = request.form['fecha']
    multasprestamo.insertar()
    flash('multa registrado exitosamente')
    return redirect(url_for('consultarMultasPrestamo'))




@app.route('/multasprestamo/ver/<int:id>')
#@login_required
def editarMultasPrestamo(id):
    multasprestamo = MultasPrestamo()
    catalogo = CatalogoMultas()
    prestamo = Prestamo()
    return render_template('/multasprestamo/editar.html', mult=multasprestamo.consultaIndividual(id),cat=catalogo.consultaGeneral(), pre=prestamo.consultaGeneral())



@app.route('/multasprestamo/editandoMultasPrestamo', methods=['post'])
#@login_required
def editandoMultasPrestamo():
    try:
        multasprestamo = MultasPrestamo()
        multasprestamo.idMultasPrestamo = request.form['idMultasPrestamo']
        multasprestamo.idCatalogoMultas = request.form['idCatalogoMultas']
        multasprestamo.idPrestamo = request.form['idPrestamo']
        multasprestamo.cantPagar = request.form['cantPagar']
        multasprestamo.fecha = request.form['fecha']
        multasprestamo.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/multasprestamo/consultar.html', mult=multasprestamo.consultaGeneral())

# ________________________________________________________________________________
# --------------------------------Membresias-------------------------------------
# ________________________________________________________________________________

@app.route('/membresias/consultarMembresias')
#@login_required
def consultarMembresias():
    membresias=Membresias()
    return render_template('/membresias/consultar.html', memb=membresias.consultaGeneral())



@app.route('/membresias/registrarMembresias')
# @login_required
def registrarMembresias():
    return render_template('/membresias/nuevo.html')


@app.route('/membresias/guardandoMembresias', methods=['post'])
# @login_required
def guardandoMembresias():
    membresias = Membresias()
    membresias.nombre = request.form['nombre']
    membresias.precio = request.form['precio']
    membresias.duracion = request.form['duracion']
    membresias.cantidadLibros=request.form['cantidadLibros']
    membresias.estatus = request.form['estatus']
    membresias.insertar()
    flash('Membresia registrada exitosamente')
    return redirect(url_for('consultarMembresias'))


@app.route('/membresias/ver/<int:id>')
#@login_required
def editarMembresias(id):
    membresias = Membresias()
    return render_template('/membresias/editar.html', memb=membresias.consultaIndividual(id))


@app.route('/membresias/editandoMembresias', methods=['post'])
#@login_required
def editandoMembresias():
    try:
        membresias = Membresias()
        membresias.idMembresias = request.form['idMembresias']
        membresias.nombre = request.form['nombre']
        membresias.precio = request.form['precio']
        membresias.duracion = request.form['duracion']
        membresias.cantidadLibros = request.form['cantidadLibros']
        membresias.estatus = request.form['estatus']
        membresias.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/membresias/consultar.html', memb=membresias.consultaGeneral())



@app.route('/membresias/eliminarMembresias/<int:id>')
#@login_required
def eliminarMembresias(id):
    membresias = Membresias()
    membresias.eliminar(id)
    flash('Registro de la Membresia eliminado con exito')
    return redirect(url_for('consultarMembresias'))

# ________________________________________________________________________________
# --------------------------------usuarios-------------------------------------
# ________________________________________________________________________________

@app.route('/usuarios/consultarUsuarios')
#@login_required
def consultarUsuarios():
    usuarios=Usuarios()
    return render_template('/usuarios/consultar.html', usu=usuarios.consultaGeneral())

@app.route('/usuarios/registrarUsuarios')
# @login_required
def registrarUsuarios():
    return render_template('/usuarios/nuevo.html')


@app.route('/usuarios/guardandoUsuarios', methods=['post'])
# @login_required
def guardandoUsuarios():
    usuarios = Usuarios()
    usuarios.nodedocumento= request.form['nodedocumento']
    usuarios.nombreCompleto = request.form['nombreCompleto']
    usuarios.appaterno = request.form['appaterno']
    usuarios.apmaterno=request.form['apmaterno']
    usuarios.sexo = request.form['sexo']
    usuarios.direccion = request.form['direccion']
    usuarios.telefono = request.form['telefono']
    usuarios.email = request.form['email']
    usuarios.insertar()
    flash('Usuario registrado exitosamente')
    return redirect(url_for('consultarUsuarios'))

# ________________________________________________________________________________
# --------------------------------autor-------------------------------------
# ________________________________________________________________________________


@app.route('/autor/consultarAutor')
#@login_required
def consultarAutor():
    autor=Autor()
    return render_template('/autor/consultar.html', aut=autor.consultaGeneral())

@app.route('/autor/registrarAutor')
# @login_required
def registrarAutor():
    return render_template('/autor/nuevo.html')


@app.route('/autor/guardandoAutor', methods=['post'])
# @login_required
def guardandoAutor():
    autor = Autor()
    autor.pais = request.form['pais']
    autor.nombre = request.form['nombre']
    autor.ciudad = request.form['ciudad']
    autor.anioNacimiento=request.form['anioNacimiento']
    autor.estudios = request.form['estudios']
    autor.insertar()
    flash('Autor registrado exitosamente')
    return redirect(url_for('consultarAutor'))

@app.route('/autor/ver/<int:id>')
#@login_required
def editarAutor(id):
    autor = Autor()
    return render_template('/autor/editar.html', aut=autor.consultaIndividual(id))


@app.route('/autor/editandoAutor', methods=['post'])
#@login_required
def editandoAutor():
    try:
        autor = Autor()
        autor.idAutor=request.form['idAutor']
        autor.pais = request.form['pais']
        autor.nombre = request.form['nombre']
        autor.ciudad = request.form['ciudad']
        autor.anioNacimiento = request.form['anioNacimiento']
        autor.estudios = request.form['estudios']
        autor.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/autor/consulat.html', aut=autor.consultaGeneral())



@app.route('/autor/eliminarAutor/<int:id>')
#@login_required
def eliminarAutor(id):
    autor = Autor()
    autor.eliminar(id)
    flash('Registro del Autor eliminado con exito')
    return redirect(url_for('consultarAutor'))


# ________________________________________________________________________________
# --------------------------------bibliotecario-------------------------------------
# ________________________________________________________________________________


@app.route('/bibliotecario/consultarBibliotecario')
#@login_required
def consultarBibliotecario():
    bibliotecario = Bibliotecario()
    return render_template('/bibliotecario/consultar.html', bibl=bibliotecario.consultaGeneral())

@app.route('/bibliotecario/registrarBibliotecario')
# @login_required
def registrarBibliotecario():
    return render_template('/bibliotecario/nuevo.html')


@app.route('/bibliotecario/guardandoBibliotecario', methods=['post'])
# @login_required
def guardandoBibliotecario():
    bibliotecario=Bibliotecario()
    bibliotecario.nombre = request.form['nombre']
    bibliotecario.password_hash = request.form['password']
    bibliotecario.tipo = request.form['tipo']
    bibliotecario.estado = request.form['estado']
    bibliotecario.horario_trabajo = request.form['horario_trabajo']
    bibliotecario.insertar()
    flash('Autor registrado exitosamente')
    return redirect(url_for('consultarAutor'))

@app.route('/bibliotecario/ver/<int:id>')
#@login_required
def editarBibliotecario(id):
    autor = Bibliotecario()
    return render_template('/bibliotecario/editar.html', bibl=Bibliotecario.consultaIndividual(id))


@app.route('/bibliotecario/editandoBibliotecario', methods=['post'])
#@login_required
def editandoBibliotecario():
    try:
        bibliotecario = Bibliotecario()
        bibliotecario.nombre = request.form['nombre']
        bibliotecario.password_hash = request.form['password']
        bibliotecario.tipo = request.form['tipo']
        bibliotecario.estado = request.form['estado']
        bibliotecario.horario_trabajo = request.form['horario_trabajo']
        bibliotecario.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/bibliotecario/consultar.html', bibl=bibliotecario.consultaGeneral())



@app.route('/bibliotecario/eliminarBibliotecario/<int:id>')
#@login_required
def eliminarBibliotecario(id):
    bibliotecario = Bibliotecario()
    bibliotecario.eliminar(id)
    flash('Registro del Bibliotecario eliminado con exito')
    return redirect(url_for('consultarBibliotecario'))


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

# -----------------------------------------------------------------------------------
# --------------------------------Prestamo-------------------------------------
# ________________________________________________________________________________
@app.route('/prestamo/consultarPrestamo')
# @login_required
def consultarPrestamo():
    bibliotecario = Biblioteacario()
    usuarios = Usuarios()
    prestamo = Prestamo()
    return render_template('/prestamo/consultar.html', pre=prestamo.consultaGeneral(), usu=usuarios.consultaGeneral(),
                           bib=bibliotecario.consultaGeneral())


@app.route('/prestamo/registrarPrestamo')
# @login_required
def registrarPrestamo():
    bibliotecario = Biblioteacario()
    usuarios = Usuarios()
    return render_template('/prestamo/nuevo.html', usu=usuarios.consultaGeneral(), bib=bibliotecario.consultaGeneral())


@app.route('/prestamo/guardandoPrestamo', methods=['post'])
# @login_required
def guardandoPrestamo():
    prestamo = Prestamo()
    prestamo.idUsuarios = request.form['idUsuarios']
    prestamo.idBibliotecario = request.form['idBibliotecario']
    prestamo.fechaprestamo = request.form['fechaprestamo']
    prestamo.fechadevolucion = request.form['fechadevolucion']
    prestamo.estatus = request.form['estatus']
    prestamo.insertar()
    flash('prestamo registrado exitosamente')
    return redirect(url_for('consultarPrestamo'))

@app.route('/prestamo/ver/<int:id>')
# @login_required
def editarPrestamo(id):
    bibliotecario = Biblioteacario()
    usuarios = Usuarios()
    prestamo = Prestamo()
    return render_template('/prestamo/editar.html', pre=prestamo.consultaIndividual(id),usu=usuarios.consultaGeneral(),bib=bibliotecario.consultaGeneral())


@app.route('/prestamo/editandoPrestamo', methods=['post'])
# @login_required
def editandoPrestamo():
    try:
        bibliotecario = Biblioteacario()
        usuarios = Usuarios()
        prestamo = Prestamo()
        prestamo.idPrestamo = request.form['idPrestamo']
        prestamo.idUsuarios = request.form['idUsuarios']
        prestamo.idBibliotecario = request.form['idBibliotecario']
        prestamo.fechaprestamo = request.form['fechaprestamo']
        prestamo.fechadevolucion = request.form['fechadevolucion']
        prestamo.estatus = request.form['estatus']
        prestamo.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/prestamo/consultar.html',  pre=prestamo.consultaGeneral(), usu=usuarios.consultaGeneral(),
                           bib=bibliotecario.consultaGeneral())


@app.route('/prestamo/eliminarPrestamo/<int:id>')
# @login_required
def eliminarPrestamo(id):
    prestamo = Prestamo()
    prestamo.eliminar(id)
    flash('Registro de Multas Prestamo eliminado con exito')
    return redirect(url_for('consultarPrestamo'))


@app.route('/prestamo/eliminarLogicaPrestamo/<int:id>')
# @login_required
def eliminarLogicaPrestamo(id):
    prestamo = Prestamo()
    prestamo.eliminacionLogica(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarPrestamo'))