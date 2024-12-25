from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# インメモリでTODOを保存
TODOS = []

@app.route('/')
def index():
    return render_template('index.html', todos=TODOS)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form.get('todo')
    if todo:
        TODOS.append(todo)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)