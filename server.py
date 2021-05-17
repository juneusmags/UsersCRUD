from flask import Flask, render_template, redirect, request
from mysqlconnection import MySQLConnection, connectToMySQL# import the function that will return an instance of a connection
app = Flask(__name__)

@app.route("/users")
def index():
    mysql= connectToMySQL('users_schema3')
    users= mysql.query_db('SELECT * FROM users;')
    return render_template("index.html", all_users=users)

@app.route("/users/<id>")
def show(id):
    mysql = connectToMySQL('users_schema3')
    query = 'SELECT * FROM users WHERE id=%(id)s;'
    data = {
        "id" : int(id)
    }
    user = mysql.query_db(query, data)
    return render_template("UsersRead.html", user = user)





@app.route("/users/new")
def index2():
    return render_template("Create.html")



@app.route("/users/new/create", methods=["POST"])
def create():
    mysql= connectToMySQL('users_schema3')
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(em)s, NOW(), NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"],
        }

    newuser = mysql.query_db(query,data)
    print(newuser,'test')
    return redirect(f"/users/{newuser}")


@app.route("/delete/<id>")
def delete(id):
    mysql = connectToMySQL('users_schema3')
    query = "DELETE FROM users WHERE id = %(id)s"
    data = {
        "id" : int(id)
    }
    mysql.query_db(query, data)
    return redirect("/users")


@app.route("/users/<id>/edit")
def update(id):
    mysql = connectToMySQL('users_schema3')
    query = 'SELECT * FROM users WHERE id=%(id)s;'
    data = {
        "id" : int(id)
    }
    user = mysql.query_db(query, data)
    return render_template("edit.html", user = user[0])



@app.route("/update/<id>", methods=["POST"])
def update2(id):
    mysql = connectToMySQL('users_schema3')
    query = "UPDATE users SET first_name=%(fn)s, last_name = %(ln)s, email = %(em)s WHERE id = %(id)s;"
    data={
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "em": request.form["email"],
        "id": int(id)
    }
    mysql.query_db(query, data)
    return redirect(f"/users/{id}")















if __name__ == "__main__":
    app.run(debug=True)