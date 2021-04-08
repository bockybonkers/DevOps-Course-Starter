from todo_app.data.session_items import add_item, get_items
from flask import Flask
from flask import request
from flask import render_template
from werkzeug.utils import redirect
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.html', headers=['id', 'status', 'title'], results=get_items())


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form['input']
        add_item(data)
        return redirect('/')
    if request.method == 'GET':
        return render_template('add.html')


if __name__ == '__main__':
    app.run()
