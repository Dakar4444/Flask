from flask import Flask, render_template, redirect, make_response, request, session, url_for


app = Flask(__name__)
app.secret_key = "WeryLongSeretKey"


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Страница с формой ввода
    пользовательских данных
    """                                         
    if request.method == "POST":                             # Если метод запроса POST
        response = make_response("Cookies")
        username = request.form.get("username")              # Получаем username и email  из формы
        email = request.form.get("email")
        if len(email) != 0 and len(username) != 0:           # Проверяем что данные введены
            response.set_cookie("username", value="username", max_age=None)    
            response.set_cookie("email", value="email", max_age=None)        # Создаем cookie почты и username
            session["usename"] = username 
            session["email"]   = email                                # Создаем сессию пользователя с email и username
            return redirect(url_for("user", username=username))
        return redirect(url_for("index"))                           # переход на страницу пользователя
    return render_template("index.html")       


@app.route("/user/<string:username>/", methods=["GET", "POST"])
def user(username, *args, **kwargs):
    """
    Старница приветствия ползователя
    """                                      
    if session:                             # Проверка наличия сесии               
        if request.method == "POST":                          # Если метод Post (кнопка выход)
            response = make_response("Cookie clear")
            if request.cookies.get("sessionid") and request.cookies.get("session"):   # Проверяем наличие cookie сессии
                response.set_cookie("csrftoken", "", expires=0)       
                response.set_cookie("sessionid", "", expires=0)         # Очищаем cookie сесиии
                response.set_cookie("session",'',expires=0)
                print('Cookie удалены')
                session.clear()                                   # Удалаяем сессию
                return redirect(url_for("index"))               # Возвращаемся на стартовую страницу
            print(request.cookies)
            print(response)
            print("Не удалось очистить Cookie")
            return redirect(url_for("index"))
        return render_template("user.html", username=username)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)