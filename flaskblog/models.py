from datetime import datetime
from os import abort
from itsdangerous import TimedSerializer
from flask import current_app, abort
from flaskblog import db, login_manager, admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView

from flask_login import current_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    
    registration_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, unique = False, nullable = False,  default=False)
    is_author = db.Column(db.Boolean, unique = False, nullable = False,  default=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    user_level = db.Column(db.Integer, nullable=False, default=0)

    lifetime_sub = db.Column(db.Boolean, unique = False, nullable = True,  default=False)
    donation_tier = db.Column(db.Integer, nullable=False, default=0)

    password = db.Column(db.String(60), nullable=False)
    

    def get_reset_token(self):
        s = TimedSerializer(current_app.config['SECRET_KEY'], salt=b'itsdangerous.Signer',)
        return s.dumps({'user_id': self.id})
        
    @staticmethod
    def verify_reset_token(token, expired_sec=900):
        s = TimedSerializer(current_app.config['SECRET_KEY'], salt=b'itsdangerous.Signer',)
        try:
            user_id = s.loads(token, max_age=expired_sec)['user_id']
        except Exception:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    link = db.Column(db.String(100), nullable=True)
    stock = db.Column(db.Text, nullable=True)
    current_price = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

 
class Globetrotting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    link = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)

    def __repr__(self):
        return f"Globetrotting('{self.stock}', '{self.price}')"


class Besteaktien(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    fullname = db.Column(db.Text, nullable=False)
    five_y_per_score = db.Column(db.Integer, nullable=False)
    Umsatz_v = db.Column(db.Float, nullable=True)
    Gewinn_v = db.Column(db.Float, nullable=True)
    five_y_u = db.Column(db.Float, nullable=True)
    five_y_g = db.Column(db.Float, nullable=True)
    five_y_kgv = db.Column(db.Float, nullable=True)
    baqs = db.Column(db.Integer, nullable = True)
    name = db.Column(db.Text, nullable=True)
    peg = db.Column(db.Float, nullable=True)


    
    def __repr__(self):
        return f"Besteaktien('{self.stock}', '{self.fullname}')"


class AdminViewUser(ModelView):
    column_searchable_list = ['username', 'email']

    def is_accessible(self):
        if current_user.is_admin == True:
            return current_user.is_authenticated
        else:
           return abort(404)

class AdminViewStocks(ModelView):
    column_searchable_list = ['stock', 'name']
    column_filters = ['stock', 'baqs']

    def is_accessible(self):
        if current_user.is_admin == True:
            return current_user.is_authenticated
        else:
           return abort(404)



admin.add_view(AdminViewUser(User, db.session))
admin.add_view(AdminViewStocks(Besteaktien, db.session))
#admin.add_view(AdminView(Post, db.session))
#admin.add_view(AdminView(Globetrotting, db.session))


