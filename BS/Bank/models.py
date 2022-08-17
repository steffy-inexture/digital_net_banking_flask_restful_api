from datetime import datetime
from sqlalchemy.orm import relationship
from BS import db


class Bank(db.Model):
    __tablename__ = "bank"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False, default='SJK BANK')
    email = db.Column(db.String(200), unique=True, nullable=False, default='sjkbank@gmail.com')
    contact = db.Column(db.String(200), default='10058')

    def __repr__(self):
        return f"Bank('{self.id}','{self.name}','{self.email}','{self.contact}')"


class Atm(db.Model):
    __tablename__ = "atm"
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), unique=True, nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"Atm('{self.id}','{self.address}')"


class Branches(db.Model):
    __tablename__ = "branch"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id', ondelete='CASCADE'), nullable=False)

    account = relationship("Account", cascade="all, delete", backref='branch', lazy='dynamic')

    def __repr__(self):
        return f"Branches('{self.id}','{self.name}','{self.address}')"


class Account(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.BigInteger, nullable=False)
    status = db.Column(db.String(100), nullable=False, default='Inactive')
    balance = db.Column(db.Float, nullable=False, default=5000)
    saving = db.Column(db.Float, nullable=False, default=0.0)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    type_id = db.Column(db.Integer, db.ForeignKey('account_type.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id', ondelete='CASCADE'), nullable=False)

    users = relationship("User", backref='account')


class AccountType(db.Model):
    __tablename__ = "account_type"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)

    account = relationship("Account", cascade="all, delete", backref='account_type', lazy='dynamic')
