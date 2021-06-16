from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy,sqlalchemy,orm
from pymongo import 



apps = Flask(__name__)
apps.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/blog'
apps.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(apps);

class Contacts(db.Model):
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(40), unique=True, nullable=False,primary_key=True)
    phone=db.Column(db.String(13),nullable=True)
    message=db.Column(db.String(213))



@apps.route('/') 
def home():
    return render_template('index.html') 

@apps.route('/about')
def about():
    return render_template('about.html')

@apps.route('/contact',methods=['POST','GET']) 
def contact():
    
    if(request.method=="POST"):

        name = request.form.get('name')
        address = request.form.get('email')
        message = request.form.get('msg')
        phone = request.form.get('phone')
        guest = Contacts(name=name, address=address,phone=phone,message=message)
        print(name)
        print(guest.name)
        db.session.add(guest)
        db.session.commit()



    return render_template('contact.html')
    
@apps.route('/post')
def route():
    return render_template('post.html')

apps.run(debug=True)