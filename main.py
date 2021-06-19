from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json
#from flask_mail import Mail
with open('config.json','r') as c:
    params=json.load(c)["params"]




apps = Flask(__name__)
apps.config['SQLALCHEMY_DATABASE_URI'] =params['local_sql_url']
apps.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(apps)

# class for sharing contacts
class Contacts(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(40), unique=True, nullable=False,primary_key=False)
    phone=db.Column(db.String(13),nullable=True)
    message=db.Column(db.String(213))

#class for getting blogs
class Blogs(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    slug = db.Column(db.String(30), unique=True, )
    title = db.Column(db.String(40))
    content=db.Column(db.String(500),)
    date_creation=db.Column(db.String(12))
    subtitle= db.Column(db.String(80))
    image_url= db.Column(db.String(80))

#Routings

@apps.route('/') 
def home():
    posts=Blogs.query.filter_by().all()[0:5]
    return render_template('index.html',facebook=params['facebook_url'],git=params['git_url'],twitter=params['twitter_url'],posts=posts) 

@apps.route('/about')
def about():
    return render_template('about.html',about=params['about_me'])

@apps.route('/post/<string:post_slug>')
def post_route(post_slug):
    post=Blogs.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params = params ,post=post)
    

@apps.route('/contact',methods=['POST','GET']) 
def contact():

    
    if(request.method=="POST"):

        name = request.form.get('name')
        address = request.form.get('email')
        message = request.form.get('msg')
        phone = request.form.get('phone')
        guest = Contacts(name=name, address=address,phone=phone,message=message)
        db.session.add(guest)
        db.session.commit()



    return render_template('contact.html',facebook=params['facebook_url'],git=params['git_url'],twitter=params['twitter_url'])
    


apps.run(debug=True)