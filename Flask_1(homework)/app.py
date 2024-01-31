from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clothers')
def clothers_page():
    return render_template('clothers.html')

@app.route('/hats')
def hats_page():
    return render_template('hats.html')

@app.route('/boots')
def boots_page():
    return render_template('boots.html')

if __name__ == '__main__':
    app.run()