from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo():
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_dojo(cls, data):
        mysql = connectToMySQL('dojos_and_ninjas_schema')
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return mysql.query_db(query, data)

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        if results:
            return cls(results[0])

    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        if results:
            dojo = cls(results[0])
            if results[0]["ninjas.id"]:
                dojo.ninjas = []
                for row in results:
                    data = {
                        "id": row["ninjas.id"],
                        "first_name": row["first_name"],
                        "last_name": row["last_name"],
                        "age": row["age"],
                        "created_at": row["ninjas.created_at"],
                        "updated_at": row["ninjas.updated_at"],
                        "dojo_id": row["dojo_id"],
                    }
                    temp_ninja = ninja.Ninja(data)
                    dojo.ninjas.append(temp_ninja)
            return dojo