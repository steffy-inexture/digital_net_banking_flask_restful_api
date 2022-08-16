from BS import db


class Bank(db.Model):

    """
        All bank's personal detail stored in BankDetails table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False, default='SJK BANK')
    email = db.Column(db.String(200), unique=True, nullable=False, default='sjkbank@gmail.com')
    contact = db.Column(db.String(200), default='10058')

    def __repr__(self):
        return f"Bank('{self.id}','{self.name}','{self.email}','{self.contact}')"


class Atm(db.Model):
    """
        Atm detail
    """
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), unique=True, nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"Atm('{self.id}','{self.address}')"

class Branches(db.Model):
    """
        Branch detail
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    address = db.Column(db.String(120), unique=True, nullable=False)
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f"Branches('{self.id}','{self.name}','{self.address}')"




