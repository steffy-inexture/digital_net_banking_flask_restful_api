from BS import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(), nullable=False)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    user_dob = db.Column(db.Date(), nullable=False)
    user_address = db.Column(db.Text, nullable=False)
    user_password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"User('{self.user_id}','{self.user_name}')"
