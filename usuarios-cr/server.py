from flask import Flask, render_template, redirect, request, session, flash
from datetime import datetime
from users import Userscr


app = Flask(__name__)
app.secret_key = 'secretninja'


@app.route("/")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    usuarios = Userscr.get_all()

    for i in usuarios:
      print(str(i.id) + " " + i.first_name + " " + i.last_name + " " + i.email,flush=True)
    return render_template("index.html", usuarios_cr = usuarios)

@app.route("/limpiar")
def limpiar():
    session.clear()
    flash("se limpio la session","info")
    return redirect("/")

@app.route('/form_insert')
def insertar():
      return render_template("form_insertar.html")

@app.route('/grabar', methods=['POST'])
def grabar():

  datos =  {
    'first_name':request.form['nombre_usuario'],'last_name':request.form['apellido_usuario'],
    'email':request.form['email_usuario'],'created_at':datetime.today(),'updated_at':datetime.today()
  }

  print(datos,flush=True)

  #se graba en el el objeto de la clase Userscr
  Userscr.save(datos)

  flash("se inserto el registro en la base de datos","info")

  return redirect("/limpiar")


if __name__ == "__main__":
    app.run(debug=True)