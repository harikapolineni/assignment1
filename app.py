from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'

db = SQLAlchemy(app)

class projectAdd(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    date_posted = db.Column(db.DateTime)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/project')
def project():
    posts = projectAdd.query.order_by(projectAdd.date_posted.desc()).all()
    return render_template('project.html', posts=posts)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    description = request.form['description']


    post = projectAdd(title=title, description=description, date_posted=datetime.now())

    db.create_all()
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('project'))



if __name__ == '__main__':
    app.run(debug=True)