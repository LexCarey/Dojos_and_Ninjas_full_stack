from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja

#TEMPLATE ROUTES
@app.route('/ninjas')
def new_ninja():
    mysql = connectToMySQL('dojos_and_ninjas_schema')
    dojos = mysql.query_db("SELECT * FROM dojos;")
    return render_template("create_ninja.html", dojos = dojos)


#ACTION ROUTES
@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    Ninja.create_ninja(request.form)
    id = request.form["dojo_id"]
    return redirect(f'/dojos/{id}')
