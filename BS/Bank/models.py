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
    card = relationship("Cards", cascade="all, delete", backref='account', lazy='dynamic')


class AccountType(db.Model):
    __tablename__ = "account_type"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)

    account = relationship("Account", cascade="all, delete", backref='account_type', lazy='dynamic')


class Cards(db.Model):
    __tablename__ = "card"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.BigInteger, default=1000)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    expiry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    cvv_number = db.Column(db.Integer, nullable=False)
    card_pin = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.String(100), nullable=False, default="Inactive")

    account_id = db.Column(db.BigInteger, db.ForeignKey('account.id', ondelete='CASCADE'),
                           nullable=False)


class LoanTypes(db.Model):
    """
        Any loan has its type which is stored in LoanType table
        can be stored here associated with particular Loan id and its type
    """
    __tablename__ = 'loan_types'
    id = db.Column(db.Integer, primary_key=True)
    type_for_loan = db.Column(db.String(100), nullable=False)
    rate_interest = db.Column(db.Float, nullable=False, default=0.0)

    loan = relationship("Loans", cascade="all, delete", backref='loan_types', lazy='dynamic')

class Loans(db.Model):
    """
        User's loan details stored in Loan table
    """
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False, default=0.0)
    status = db.Column(db.String(100), nullable=False, default='Inactive')
    paid_amount = db.Column(db.Float, nullable=False, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    loan_type_id = db.Column(db.Integer, db.ForeignKey('loan_types.id', ondelete='CASCADE'), nullable=False)

class InsuranceTypes(db.Model):
    """
        InsuranceType detail
    """
    __tablename__ = 'insurance_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    monthly_pay = db.Column(db.Float, nullable=False, default=0.0)
    insurance = relationship("Insurances", cascade="all, delete", backref='insurance_types', lazy='dynamic')

    def __repr__(self):
        return f"Insurance_types('{self.id}','{self.name}','{self.monthly_pay}')"

class Insurances(db.Model):
    __table_name__='insurances'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False, default=0.0)
    status = db.Column(db.String(100), nullable=False, default='Inactive')
    claim_status = db.Column(db.String(100), nullable=False, default='Not claimed')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    insurance_type_id = db.Column(db.Integer, db.ForeignKey('insurance_types.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"Insurance('{self.id}','{self.amount}','{self.status}')"