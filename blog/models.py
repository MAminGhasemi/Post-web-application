from blog import db
from sqlalchemy import CheckConstraint
from datetime import datetime
from flask_login import UserMixin 

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(35),unique=True,nullable=False)
    email=db.Column(db.String(255),unique=True,nullable=False)
    password=db.Column(db.String(100),nullable=False)
    user_pic=db.Column(db.String(20),nullable=True)
    posts = db.relationship( 'Post',backref='author', lazy=True)

    # __table_args__ = (CheckConstraint('length(password) > 8', name='password_length_constraint'))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id} => {self.email})"
    
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(25),nullable=False)
    content=db.Column(db.Text,nullable=False)
    date=db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id} => {self.title} by {self.user_id})"


    


    
