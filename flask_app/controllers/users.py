from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route("/")
def index():
    return redirect('/users')

@app.route("/users")
def read():
    users=User.get_all()
    return render_template('read.html', all_users = users)

@app.route("/users/form")
def forms():
    return render_template('create.html')

@app.route("/users/new", methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect("/users")

@app.route("/users/show/<int:id>")
def show(id):
    data={
        "id":id
    }
    return render_template('show.html', user=User.get_one(data))

@app.route("/users/edit/<int:id>")
def edit(id):
    data={
        "id":id
    }
    return render_template("edit.html", user=User.get_one(data))


@app.route('/users/update',methods=['POST'])
def update():
    User.update(request.form)
    print(User.update(request.form))
    return redirect('/users')

@app.route('/users/delete/<int:id>')
def delete(id):
    data={
        'id':id
    }
    User.destroy(data)
    return redirect('/users')
