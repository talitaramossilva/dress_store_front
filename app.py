from ctypes import pythonapi
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


dresses = [
    {"id": 1, "name": "Vestido Azul", "size": "M", "color": "Azul"},
    {"id": 2, "name": "Vestido Vermelho", "size": "S", "color": "Vermelho"},
]

@app.route('/')
def index():
    return render_template('index.html', dresses=dresses)

@app.route('/add_dress', methods=['POST'])
def add_dress():
    name = request.form['name']
    size = request.form['size']
    color = request.form['color']

    if name and size and color:
        new_dress = {"id": len(dresses) + 1, "name": name, "size": size, "color": color}
        dresses.append(new_dress)

    return redirect(url_for('index'))

@app.route('/search_dress', methods=['POST'])
def search_dress():
    search_query = request.form['search_query']
    if search_query:
        search_results = [dress for dress in dresses if search_query.lower() in dress['name'].lower()]
        dresses.clear()
        dresses.extend(search_results)

    return redirect(url_for('index'))

@app.route('/remove_dress/<int:dress_id>')
def remove_dress(dress_id):
    global dresses
    dresses = [dress for dress in dresses if dress['id'] != dress_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


