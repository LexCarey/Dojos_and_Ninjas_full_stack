from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

#TEMPLATE ROUTES
@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    dojos = mysql.query_db("SELECT * FROM dojos;")
    print(dojos)
    return render_template("index.html", dojos = dojos)

@app.route('/dojos/<int:id>')
def single_dojo(id):
    dojo = Dojo.get_dojo_ninjas({ "id": id })
    return render_template("single_dojo.html", dojo = dojo)


#ACTION ROUTES
@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')
