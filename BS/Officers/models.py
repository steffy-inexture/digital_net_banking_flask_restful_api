from BS import db


class LoanTypes(db.Model):
    """
        Loantype detail
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rate_interest = db.Column(db.String(320), nullable=False, default='0.0')

    def __repr__(self):
        return f"Atm('{self.id}','{self.name}','{self.rate_interest}')"


class InsuranceTypes(db.Model):
    """
        InsuranceType detail
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    monthly_pay = db.Column(db.String(120), nullable=False, default='0.0')

    def __repr__(self):
        return f"Atm('{self.id}','{self.name}','{self.monthly_pay}')"
