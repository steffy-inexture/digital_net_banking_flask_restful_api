import random

from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from flask_mail import Message

from BS import mail, db
from BS.Bank.models import OtpByMail, Loans, Transactions
from BS.User.models import User
from BS.factory import celery


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
    data = OtpByMail(sender_id=user.id, email=user.email, otp=otp, transaction_id=transaction_id)
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
    mail.send(msg)


@celery.task()
def send_mail_for_successfull(transaction_id):
    transaction = Transactions.query.filter_by(id=transaction_id).first()
    if not transaction:
        return jsonify({'message': 'This transaction data is not available..'})
    sender = User.query.filter_by(id=transaction.sender_id).first()
    receiver = User.query.filter_by(id=transaction.receiver_id).first()
    if not sender:
        return jsonify({'message': 'User data for sender is not available...'})
    if not receiver:
        return jsonify({'message': 'User data for receiver is not available...'})
    msg = Message('Transaction details is here: ', sender='steffykhristi.18.ce@iite.indusuni.ac.in',
                  recipients=[sender.email])
    msg.body = f'''Hey {sender.user_name}.. your transaction has been successfull done..
    Transaction details:
    transaction id = {transaction.id}
    transaction amount = {transaction.amount}
    Sender name : {sender.user_name}
    Receiver name : {receiver.user_name}
    Date of transaction :{transaction.date}
    Transaction status : {transaction.is_transfer}
    If you did not make this request then just ignore this msg and no change will be there.
    '''
    msg2 = Message('Transaction details is here: ', sender='steffykhristi.18.ce@iite.indusuni.ac.in',
                   recipients=[receiver.email])
    msg2.body = f'''Hey {receiver.user_name}.. You received money from transaction kindly check below details..
        Transaction details:
        transaction id = {transaction.id}
        transaction amount = {transaction.amount}
        Sender name : {sender.user_name}
        Receiver name : {receiver.user_name}
        Date of transaction :{transaction.date}
        Transaction status : {transaction.is_transfer}
        If you did not make this request then just ignore this msg and no change will be there.
        '''
    mail.send(msg)
    mail.send(msg2)
