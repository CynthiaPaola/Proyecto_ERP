import datetime
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from flask_login import current_user,login_user,logout_user,login_manager,login_required,LoginManager
from model.DAO import db, CatalogoMultas, Categorias, Proveedores,Editorial,Membresias
app=Flask(__name__, template_folder='../view', static_folder='../static')
Bootstrap(app)
#---------------------Conexion ESPINOZA-----------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://user_erpbiblioteca:toni@localhost/erpbiblioteca'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
#________________________________________________________________________________
#--------------------------------COMUNES-----------------------------------------
#________________________________________________________________________________
@login_manager.user_loader
def load_user(id):
    return CatalogoMultas.query.get(int(id))

@app.route('/')
def login():
    return render_template('common/login.html')

@app.route('/index')
#@login_required
def inicio():
    return render_template('common/index.html')
#________________________________________________________________________________
#--------------------------------catalogoMultas----------------------------------
#________________________________________________________________________________
@app.route('/catalogoMultas/consultarCatalogoMultas')
#@login_required
def consultarCatalogoMultas():
    catalogo = CatalogoMultas()
    return render_template('/catalogoMultas/consultar.html', catal=catalogo.consultaGeneral())

@app.route('/catalogoMultas/registrarCatalogoMultas')
#@login_required
def registrarCatalogoMultas():
    return render_template('/catalogoMultas/nuevo.html')

@app.route('/catalogoMultas/guardandoCatalogoMultas',methods=['post'])
#@login_required
def guardandoCatalogoMultas():
    catalogo = CatalogoMultas()
    catalogo.nombre = request.form['nombre']
    catalogo.descripcion = request.form['descripcion']
    catalogo.precio = request.form['precio']
    catalogo.estatus = request.form['estatus']
    catalogo.insertar()
    flash('Catalogo de Multas registrado exitosamente')
    return redirect(url_for('registrarCatalogoMultas'))

@app.route('/catalogoMultas/ver/<int:id>')
#@login_required
def editarCatalogoMultas(id):
    catalogo = CatalogoMultas()
    return render_template('/catalogoMultas/editar.html', catal=catalogo.consultaIndividual(id))

@app.route('/catalogoMultas/editandoCatalogoMultas',methods=['post'])
#@login_required
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
    return render_template('/catalogoMultas/editar.html', catal=catalogo)

@app.route('/catalogoMultas/eliminarCatalogoMultas/<int:id>')
#@login_required
def eliminarCatalogoMultas(id):
    catalogo = CatalogoMultas()
    catalogo.eliminar(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarCatalogoMultas'))

#________________________________________________________________________________
#--------------------------------Categorias----------------------------------
#________________________________________________________________________________
@app.route('/categorias/consultarCategorias')
#@login_required
def consultarCategorias():
    categorias = Categorias()
    return render_template('/categorias/consultar.html', cate=categorias.consultaGeneral())
#________________________________________________________________________________
#--------------------------------Categorias empese aqui----------------------------------
#________________________________________________________________________________

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
    return redirect(url_for('registrarCategorias'))

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
    return render_template('/categorias/editar.html', cate=categorias)

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
    return redirect(url_for('registrarProveedores'))

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
    return render_template('/proveedores/editar.html', prov=proveedores)

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
    return redirect(url_for('registrarEditorial'))

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
    return render_template('/editorial/editar.html', edit=editorial)

@app.route('/editorial/eliminarEditorial/<int:id>')
#@login_required
def eliminarEditorial(id):
    editorial = Editorial()
    editorial.eliminar(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarEditorial'))


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
    return render_template('/membresias/registrarMembresias.html')


@app.route('/membresias/guardandoMembresias', methods=['post'])
# @login_required
def guardandoMembresias():
    membresias = Membresias()
    membresias.nombre = request.form['nombre']
    membresias.precio = request.form['precio']
    membresias.duracion = request.form['duracion']
    membresias.cantidadLibros = request.form['cantidadLibros']
    membresias.estatus = request.form['estatus']
    membresias.insertar()
    flash('Membresia registrada exitosamente')
    return redirect(url_for('registrarMembresias'))


@app.route('/membresias/ver/<int:id>')
#@login_required
def editarMembresias(id):
    membresias = Membresias()
    return render_template('/membresias/editarMem.html', mem=membresias.consultaIndividual(id))


@app.route('/membresias/editandoMembresias', methods=['post'])
#@login_required
def editandoMembresias():
    try:
        membresias = Membresias()
        membresias.nombre = request.form['nombre']
        membresias.precio = request.form['precio']
        membresias.duracion = request.form['duracion']
        membresias.cantidadLibros = request.form['cantidadLibros']
        membresias.fechaInicio = request.form['fechaInicio']
        membresias.fechaFin = request.form['fechaFin']
        membresias.actualizar()
        flash('Datos actualizados con exito')
    except:
        flash('!Error al actualizar!')
    return render_template('/membresias/editarMem.html', mem=membresias)

def eliminarMembresias(id):
    membresias = Membresias()
    membresias.eliminar(id)
    flash('Registro de la Membresia eliminado con exito')
    return redirect(url_for('consultarMembresias'))


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
