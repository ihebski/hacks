from flask import Flask, render_template, request, redirect
from datetime import datetime
from tinydb import TinyDB,Query,where
import tinydb
from tinydb.operations import delete
import pathlib
import uuid

app = Flask(__name__)
path = pathlib.Path(__file__).parent
db = TinyDB(f"{path}/data/notebook.json")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        notes = request.form['notes']
        try:
            db.insert({"id":str(uuid.uuid4()),"notes":notes,"created_at":str(datetime.now().date())})
            return redirect('/')
        except Exception as e:
            return "There was a problem adding new notes."+str(e)

    else:
        return render_template('index.html', notes=db.all())



@app.route('/delete/<id>')
def delete(id):
    try:
        db.remove(Query().id==id)
        return redirect('/')
    except:
        return "There was a problem deleting data."


@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    notes = db.search(Query().id == id)[0]
    print(notes)

    if request.method == 'POST':
        try:
            db.update({'notes': request.form['notes']},Query().id == id)
            return redirect('/')
        except Exception as e:
            return "There was a problem updating data."+str("")
    else:   
        title = "Update Data"
        return render_template('update.html', title=title, notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
