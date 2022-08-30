import random

from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from flask_mail import Message

from BS.factory import mail, db
from BS.Bank.models import OtpByMail, Loans
from BS.User.models import User


def send_otp_email(transaction_id):
    user = User.query.filter_by(id=get_jwt_identity()).first()
    if not user:
        return jsonify({'message': 'Sender User is not existed'})
    otp = random.randint(1111, 9999)
    msg = Message('Your OTP is here: ', sender='steffykhristi.18.ce@iite.indusuni.ac.in',
                  recipients=[user.email])
    msg.body = f'''This is the OTP as requested: :{otp}
    Kindly check the next page and enter the otp.
    If you did not make this request then just ignore this msg and no change will be there.
    '''
    mail.send(msg)
    data = OtpByMail(sender_id=user.id, email=user.email, otp=otp,transaction_id=transaction_id)
    db.session.add(data)
    db.session.commit()

    return otp

def send_mail_for_pending_loan(loan_id):
    loan = Loans.query.filter_by(id=loan_id).first()
    if not loan:
        return jsonify({'message': 'Loan data is not available for this loan id'})

    user = User.query.filter_by(id=loan.user_id).first()
    if not user:
        return jsonify({'message': 'User data is not available...'})

    msg = Message('Hey!, your loan detail is here: ', sender='steffykhristi.18.ce@iite.indusuni.ac.in',
                  recipients=[user.email])
    msg.body = f'''Hey {user.user_name}.. your loan is pending..
    Loan details:
    loan_amount = {loan.amount}
    Kindly understand that you are pending with the loan and pay it ASAP.
    If you did not make this request then just ignore this msg and no change will be there.
    '''
    otp = 123
    mail.send(msg)
    return otp
