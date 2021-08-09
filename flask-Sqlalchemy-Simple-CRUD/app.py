from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notebook.db'
db = SQLAlchemy(app)

class Utility(object):
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

# Model to deploy
class Notebook(db.Model,Utility):
    __metaclass__=Utility()
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        notes = request.form['notes']
        try:
            Notebook(notes=request.form['notes']).save()
            return redirect('/')
        except:
            return "There was a problem adding new notes."

    else:
        notes = Notebook.query.order_by(Notebook.created_at).all()
        return render_template('index.html', notes=notes)


@app.route('/delete/<int:id>')
def delete(id):
    try:
        Notebook.query.filter(Notebook.id == id).delete()
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting data."


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    notes = Notebook.query.get_or_404(id)

    if request.method == 'POST':
        try:
            Notebook.query.filter_by(id=id).update(dict(notes=request.form['notes']))
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating data."
    else:   
        title = "Update Data"
        return render_template('update.html', title=title, notes=notes)


if __name__ == '__main__':
    app.run(debug=True)
