from flask import Flask, render_template, request, redirect
import db
from models import GestorTareas

app = Flask(__name__)

#### PÁGINAS ###
@app.route('/')
def home():  # put application's code here
    tareas = db.session.query(GestorTareas).all()
    return render_template("index.html", lista_de_tareas=tareas)

#Editar Tarea
@app.route('/editar-tarea/<id>')
def showEditarTarea(id):
    tarea = db.session.query(GestorTareas).filter_by(id=id).first()

    fechalimite = str(tarea.fechalimite).replace(" 00:00:00","")
    return render_template("editar-tarea.html",tarea=tarea,fechalimite=fechalimite)


#### MÉTODOS ###
#Crear Tarea
@app.route('/crear-tarea', methods=["POST"])
def crearTarea():
    from datetime import datetime

    fechalimite = datetime.strptime(request.form['fechaExpiracion'], '%Y-%m-%d')

    tarea = GestorTareas(tarea=request.form['tarea'], categoria=request.form['categoria'],fechalimite=fechalimite,estado="En Proceso")
    db.session.add(tarea)
    db.session.commit()
    db.session.close()
    return redirect("/")

#Editar Tarea
@app.route('/editar-tarea', methods=["POST"])
def editarTarea():
    from datetime import datetime

    id = request.form['id']
    tarea = db.session.query(GestorTareas).filter_by(id=id).first()

    fechalimite = datetime.strptime(request.form['fechaExpiracion'], '%Y-%m-%d')

    tarea.tarea = request.form['tarea']
    tarea.categoria = request.form['categoria']
    tarea.fechalimite = fechalimite
    tarea.estado = "En Proceso"

    db.session.commit()
    db.session.close()
    return redirect("/")

#Cambiar Estado de Tarea
@app.route('/completar-tarea/<id>')
def completarTarea(id):
    tarea = db.session.query(GestorTareas).filter_by(id=id).first()
    tarea.estado = "Completada"

    db.session.commit()
    db.session.close()
    return redirect("/")

#Eliminar Tarea
@app.route('/eliminar-tarea/<id>')
def eliminarTarea(id):
    db.session.query(GestorTareas).filter_by(id=id).delete()

    db.session.commit()
    db.session.close()
    return redirect("/")




if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)

