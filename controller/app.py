import datetime
from urllib import request

from flask import Flask,render_template,request,flash,redirect,url_for,abort
from flask_bootstrap import Bootstrap
from flask_login import current_user,login_user,logout_user,login_manager,login_required,LoginManager
from model.DAO import db, CatalogoMultas
app=Flask(__name__, template_folder='../view', static_folder='../static')
Bootstrap(app)
#---------------------Conexion ESPINOZA-----------------------------------------
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
@login_required
def registrarCatalogoMultas():
    return render_template('/catalogoMultas/nuevo.html')

@app.route('/catalogoMultas/guardandoCatalogoMultas',methods=['post'])
@login_required
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
@login_required
def editarCatalogoMultas(id):
    catalogo = CatalogoMultas()
    return render_template('/catalogoMultas/editar.html', catal=catalogo.consultaIndividual(id))

@app.route('/catalogoMultas/editandoCatalogoMultas',methods=['post'])
@login_required
def editandoCatalogoMultas():
    try:
        catalogo = CatalogoMultas()
        catalogo.idCatalogoMultas = request.form['idEstado']
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
@login_required
def eliminarCatalogoMultas(id):
    catalogo = CatalogoMultas()
    catalogo.eliminar(id)
    flash('Registro del Catalogo de Multas eliminado con exito')
    return redirect(url_for('consultarCatalogoMultas'))

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
