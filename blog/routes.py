from blog import app,bcrypt,db,login_manager
from flask import render_template,redirect,request,url_for,flash,jsonify
from blog.forms import RegisterForm,LoginForm
from blog.models import User,Post
import base64
from flask_login import login_user,current_user,logout_user,login_required
import os
import imghdr
import random

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



def b64encode(value):
    return base64.b64encode(value).decode('utf-8')

@app.route("/")
def home():
    posts = Post.query.order_by(Post.date.desc()).all()

    return render_template("home.html",posts=posts)

@app.route("/signup",methods=['GET','POST'])
def register():

    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        existing_user = User.query.filter_by(username=username).first()
        existing_email = User.query.filter_by(email=email).first()
        
        if existing_user or existing_email:
            flash('Username or email already taken !', 'token')
            return redirect(url_for('register'))
        
        
        file = request.files['photo']
        if file:

            file_format = imghdr.what(file)
       
            new_fileName=username + "."+file_format
   
            dest_path = os.path.join('images', new_fileName)


            file.save(os.path.join(app.static_folder, dest_path))
        else:
            if request.form.get("gender") == "male":
                avatars=['av-m-1','av-m-2','av-m-3','av-m-4']
            
            else:
                avatars=['av-f-1','av-f-2','av-f-3','av-f-4']
            
            random_avatar = random.choice(avatars)
            
            new_fileName=random_avatar + ".jpg"
        
        print(new_fileName)

        hashed_pass = bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8')
        user = User(username=username, email=email, password=hashed_pass, user_pic=new_fileName)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered', 'text-success')
        login_user(user,remember=False)
        return redirect(url_for('home'))
    
    return render_template('register.html')


@app.route("/login",methods=['GET','POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':

        user=User.query.filter_by(email=request.form.get('email')).first()
        
        if user and bcrypt.check_password_hash(user.password,request.form.get('password')):
            login_user(user,remember=request.form.get("remember"))
            flash('You logged in successfully', "text-info")
            return redirect(url_for('home'))
        else:
            flash('Email or Password is incorrect !', 'token')

    return render_template("login.html")  


@app.route("/logout",methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    flash("you logged out successfully","text-info")
    return redirect(url_for('home'))


@app.route("/create",methods=['GET','POST'])
@login_required
def create():
    if request.method == 'POST':
        post=Post(title=request.form.get("title"),content=request.form.get("content"),author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Congratulations, your post has been successfully placed","text-info")
        return redirect(url_for("home"))
    return render_template("create_post.html")


@app.route('/users_count', methods=['GET'])
def get_users_count():
    count = User.query.count()
    return jsonify({'count': count})