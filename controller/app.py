import datetime
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from flask_login import current_user,login_user,logout_user,login_manager,login_required,LoginManager
from model.DAO import db, CatalogoMultas, Categorias
app=Flask(__name__, template_folder='../view', static_folder='../static')
Bootstrap(app)
#----------------------------Conexion -----------------------------------------
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/erpbiblioteca'
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
    return render_template('/categorias/consultar.html', catog=categorias.consultaGeneral())


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
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


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)

#________________________________________________________________________________
#--------------------------------Membresias-------------------------------------
#________________________________________________________________________________
@app.route ('/Membresias/consultarMembresias')
#@login_required
def consultarMembresias():
    membresias = Membresias()
    return render_template('/membresias/membresias.html', edit=membresias.consultarMembresias())

@app.route ('/membresias/registrarMembresias')
#@login_required
def registrarMembresias():
    return render_template('/membresias/registrarMembresias.html')

@app.route ('/membresias/guardandoMembresias', methods=['post'])
#@login_required
def guardandoMembresias():
    membresias = Membresias()
    membresias.nombre = request.form['nombre']
    membresias.precio = request.form['precio']
    membresias.duracion = request.form['duracion']
    membresias.cantidadLibros = request.form['cantidadLibros']
    membresias.estatus = request.form['estatus']
    membresias.insertar()
    flash ('Membresia registrada exitosamente')
    return redirect (url_for('registrarMembresia'))


@app.route('/Membresias/ver/<int:id>')
#@login_required
def mostrarMembresias(id):
    membresias = Membresias()
    return render_template('/membresias/editarMem.html', mem=membresias.consultaIndividual(id))

@app.route('/Membresias/editandoMembresias',methods=['post'])
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
    return render_template('/membresias/editarMem.html', catal=catalogo)


@app.route('/membresias/eliminarMembresias/<int:id>')
#@login_required
def eliminarMembresias(id):
    membresias = Membresias()
    membresias.eliminar(id)
    flash('Registro de la Membresia eliminado con exito')
    return redirect(url_for('consultarMembresias'))
    
