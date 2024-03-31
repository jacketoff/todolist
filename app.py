from flask import Flask, render_template, url_for, request
app = Flask(__name__)

list = []

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'task' in request.form:
            task = request.form['task']
            list.append(task)

        if 'delete' in request.form:
            item_to_delete = request.form['delete']
            list.remove(item_to_delete)

    return render_template('index.html',list=list)


