from flask import Flask, render_template, url_for, request
app = Flask(__name__)

list = []

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        list.append(task)
    
    return render_template('index.html',list=list)
#test
#test
