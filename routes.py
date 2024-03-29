from flask import Flask, render_template, redirect, url_for, session
from funciones import *  #Importando mis Funciones
from flask import request, jsonify

#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app

app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'

#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    if 'conectado' in session:
        return redirect(url_for('inicio'))
    else:
        return render_template('public/modulo_login/index.html')
    
    
#Creando mi Decorador para el Home
@app.route('/')
def inicio():
    if 'conectado' in session:
        return render_template('public/dashboard/home.html', dataLogin = dataLoginSesion())
    else:
        return render_template('public/modulo_login/index.html')
    
    
@app.route('/login')
def login():
    if 'conectado' in session:
        return render_template('public/dashboard/home.html', dataLogin = dataLoginSesion())
    else:
        return render_template('public/modulo_login/index.html')

@app.route('/catalogo')
def catalogo():
    if 'conectado' in session:
        return render_template('public/modulo_compras/index_compras.html', dataLogin = dataLoginSesion())
    else:
        return render_template('public/modulo_login/index.html')

@app.route('/carrito')
def carrito():
    if 'conectado' in session:
        return render_template('public/modulo_carrito/index_carrito.html', dataLogin = dataLoginSesion())
    else:
        return render_template('public/modulo_login/index.html')

#Ruta para editar el perfil del cliente
@app.route('/edit-profile', methods=['GET', 'POST'])
def editProfile():
    if 'conectado' in session:
        return render_template('public/dashboard/pages/Profile.html', dataUser = dataPerfilUsuario(), dataLogin = dataLoginSesion())
    return redirect(url_for('inicio'))

    
# Cerrar session del usuario
@app.route('/logout')
def logout():
    msgClose = ''
    # Eliminar datos de sesión, esto cerrará la sesión del usuario
    session.pop('conectado', None)
    session.pop('id', None)
    session.pop('email', None)
    msgClose ="La sesión fue cerrada correctamente"
    return render_template('public/modulo_login/index.html', msjAlert = msgClose, typeAlert=1)


