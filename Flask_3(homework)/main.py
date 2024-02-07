from flask import Flask, render_template, redirect, make_response, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User


app = Flask(__name__)
app.secret_key = "WeryLongSecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Страница с формой ввода
    пользовательских данных
    """                                         
    if request.method == "POST":                          
        username = request.form.get("username")              
        surname = request.form.get("surname")
        email = request.form.get("email")
        password = request.form.get("password")
        if len(username) > 4 and len(surname) > 4 and len(email) > 4 and len(password) > 4:
            hash = generate_password_hash(password)
            new_user = User(username = username, surname = surname, email = email, password = hash)
            db.session.add(new_user)
            db.session.commit()
            return render_template('user.html', username=username)
        return redirect(url_for('index'))
    return render_template('index.html')

                  
@app.route('/user/<string:username>', methods = ["GET","POST"])
def user(username):
    if session:
        if request.method == "POST":
            return redirect(url_for('index'))
        return render_template('user.html', username=username)
    return redirect(url_for('index'))
        



@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


if __name__ == "__main__":
    app.run(debug=True)