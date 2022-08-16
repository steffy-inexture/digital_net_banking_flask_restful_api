from sqlalchemy.orm import relationship

from BS import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contact = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    dob = db.Column(db.Date(), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    user_role_id = db.Column(db.Integer, db.ForeignKey('user_roles.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"User('{self.id}','{self.user_name}')"


class UserRoles(db.Model):
    """
        Different type of user roles declared here
    """
    __tablename__ = "user_roles"
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(200), nullable=False, unique=True)

    user = relationship("User", cascade="all, delete", backref='user_roles', lazy='dynamic')
