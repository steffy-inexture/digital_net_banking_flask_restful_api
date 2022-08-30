from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from marshmallow import ValidationError
from sqlalchemy import func

from BS.factory import db
from BS.Bank.models import Bank, Atm, Branches, Account, AccountType, Loans, Insurances, TransactionTypes, Transactions, \
    OtpByMail
from BS.Bank.schemas import BankDetailSchema, AtmDetailSchema, UpdateAtmDetailSchema, BranchDetailSchema, \
    UpdateBranchDetailSchema, LoanRequestSchema, InsuranceRequestSchema, TransactMoneySchema, OtpCheck, PayBack
from BS.Bank import constants
from BS.Bank.utils import send_otp_email
from BS.User.models import User


class BankDetailServices:
    @staticmethod
    def get_bank_details():
        bank_schema = BankDetailSchema()
        bank_detail = Bank.query.filter_by(id='1').first()
        json_bank_detail = bank_schema.dump(bank_detail)
        return jsonify(json_bank_detail)

    @staticmethod
    def post_bank_details():
        bank_detail_Schema = BankDetailSchema()
        bank_data = request.get_json()
        try:
            bank_post_data = bank_detail_Schema.load(bank_data)
            db.session.add(bank_post_data)
            db.session.commit()
            return jsonify({'message': constants.BANK_DETAIL_ADDED})

        except ValidationError as err:
            return jsonify(err.messages)


class AllAtmService:

    @staticmethod
    def get_all_atm_data():
        atm_schema = AtmDetailSchema(many=True)
        atm_detail = Atm.query.all()
        json_atm_detail = atm_schema.dump(atm_detail)
        return jsonify(json_atm_detail)


class ParticularAtmServices:

    @staticmethod
    def get_particular_atm(id):
        atm_schema = AtmDetailSchema()
        atm_data = Atm.query.filter_by(id=id).first()
        if atm_data:
            json_atm_detail = atm_schema.dump(atm_data)
            return jsonify(json_atm_detail)
        else:
            return jsonify(message=constants.ATM_DOES_NOT_EXIST), 404

    @staticmethod
    def delete_particular_atm(id):
        delete_atm = Atm.query.filter_by(id=id).first()
        if delete_atm:
            db.session.delete(delete_atm)
            db.session.commit()
            return jsonify(message=constants.ATM_DELETED), 200
        else:
            return jsonify(message=constants.ATM_DOES_NOT_EXIST), 404

    @staticmethod
    def put_particular_atm(id):
        atm_schema = UpdateAtmDetailSchema(only="address")
        atm_data = request.get_json()
        atm = Atm.query.filter_by(id=id).first()
        try:
            atm_schema.load(atm_data, instance=atm)
            db.session.commit()
            return jsonify({'message': constants.ATM_DATA_UPDATED})

        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def post_atm_data():
        atm_schema = AtmDetailSchema()
        atm_data = request.get_json()
        try:
            existed_atm = Atm.query.filter_by(address=atm_data['address']).first()
            if existed_atm:
                return jsonify({'message': constants.ATM_ADDRESS_ALREADY_EXISTED})
            else:
                atm_post_data = atm_schema.load(atm_data)
                bank = Bank.query.filter_by(id=1).first()
                atm_post_data.bank_id = bank.id
                db.session.add(atm_post_data)
                db.session.commit()
                return jsonify({'message': constants.NEW_ATM_ADDED})

        except ValidationError as err:
            return jsonify(err.messages)


# for branches
class BranchServices:

    @staticmethod
    def get_all_branches_data():
        branch_schema = BranchDetailSchema(many=True)
        branches_detail = Branches.query.all()
        json_data = branch_schema.dump(branches_detail)
        return jsonify(json_data)

    @staticmethod
    def get_particular_branch(id):
        branch_schema = BranchDetailSchema()
        branch_data = Branches.query.filter_by(id=id).first()
        if branch_data:
            json_branch_detail = branch_schema.dump(branch_data)
            return jsonify(json_branch_detail)
        else:
            return jsonify(message=constants.BRANCH_DOES_NOT_EXIST), 404

    @staticmethod
    def post_branch_data():
        branch_schema = BranchDetailSchema()
        branch_data = request.get_json()
        try:
            existed_branch_name = Branches.query.filter_by(name=branch_data['name']).first()
            existed_branch_address = Branches.query.filter_by(address=branch_data['address']).first()
            if existed_branch_name:
                return jsonify({'message': constants.BRANCH_NAME_TAKEN})
            elif existed_branch_address:
                return jsonify({'message': constants.BRANCH_ADDRESS_ALREADY_EXIST})
            else:
                branch_post_data = branch_schema.load(branch_data)
                bank = Bank.query.filter_by(id=1).first()
                branch_post_data.bank_id = bank.id
                db.session.add(branch_post_data)
                db.session.commit()
                return jsonify({'message': constants.BRANCH_ADDED})

        except ValidationError as err:
            return jsonify(err.messages)

    # add validation for weather this branch has allocated with some user or not afterwords [ NEEDED MODIFICATION ]
    @staticmethod
    def delete_particular_branch(id):
        delete_branch = Branches.query.filter_by(id=id).first()
        if delete_branch:
            db.session.delete(delete_branch)
            db.session.commit()
            return jsonify(message=constants.BRANCH_DELETED), 200
        else:
            return jsonify(message=constants.BRANCH_DOES_NOT_EXIST), 404

    # add validation for weather this branch has allocated with some user or not afterwords [ NEEDED MODIFICATION ]
    @staticmethod
    def put_particular_branch(id):
        branch_schema = UpdateBranchDetailSchema(only=["address", "name"])
        branch_data = request.get_json()
        branch = Branches.query.filter_by(id=id).first()
        try:
            branch_schema.load(branch_data, instance=branch)
            db.session.commit()
            return jsonify({'message': constants.BRANCH_DATA_UPDATED})

        except ValidationError as err:
            return jsonify(err.messages)


def account_creation(user_id):
    user = User.query.filter_by(id=user_id).first()
    branch = Branches.query.first()
    account = db.session.query(func.max(Account.number)).first()
    acc_type = AccountType.query.first()
    if account[0]:
        account_number = account[0] + 1
    else:
        account_number = 1000000
    account = Account(
        type_id=acc_type.id,
        number=account_number,
        user_id=user.id,
        branch_id=branch.id,
        balance=5000
    )
    db.session.add(account)
    db.session.commit()


class LoanRequestService:

    def loan_request(self):
        user_id = get_jwt_identity()
        loan_req_schema = LoanRequestSchema()
        data = request.get_json()
        try:
            already_has_loan = Loans.query.filter_by(user_id=user_id).first()
            if already_has_loan:
                return jsonify({'message': constants.USER_ALREADY_HAVE_CURRENT_LOAN}), 409
            else:
                data = loan_req_schema.load(data)
                loan = Loans(amount=data['amount'],
                             loan_type_id=data['loan_id'],
                             user_id=user_id)
                db.session.add(loan)
                db.session.commit()
                return jsonify({'message': constants.LOAN_REQUESTED_SUCCESSFULLY}), 200

        except ValidationError as err:
            return jsonify(err.messages)


class InsuranceRequestService:

    def insurance_request(self):
        user_id = get_jwt_identity()
        insurance_req_schema = InsuranceRequestSchema()
        data = request.get_json()
        try:
            already_has_insurance = Insurances.query.filter_by(user_id=user_id).first()
            if already_has_insurance:
                return jsonify({'message': constants.USER_ALREADY_HAVE_CURRENT_INSURANCE})
            else:
                data = insurance_req_schema.load(data)
                insurance = Insurances(amount=data['amount'],
                                       insurance_type_id=data['insurance_id'],
                                       user_id=user_id)
                db.session.add(insurance)
                db.session.commit()
                return jsonify({'message': constants.INSURANCE_REQUESTED_SUCCESSFULLY})

        except ValidationError as err:
            return jsonify(err.messages)


class TransactMoneyService:

    @staticmethod
    def account_transfer():
        transaction_detail_Schema = TransactMoneySchema()
        transaction_data = request.get_json()
        user_id = get_jwt_identity()
        try:
            account = Account.query.filter_by(number=transaction_data['number']).first()
            sender_acc = Account.query.filter_by(user_id=user_id).first()
            if account:
                if account.number == sender_acc.number:
                    return jsonify({'message': 'You can not transfer in your own account this does not make any sense'})
                post_transaction = transaction_detail_Schema.load(transaction_data)
                transaction_type = TransactionTypes.query.filter_by(type='Debit').first()
                if not transaction_type:
                    return jsonify({'message': constants.NO_TYPE_FOR_THIS_TRANSACTION})
                if sender_acc.balance < post_transaction['amount']:
                    return jsonify({'message': constants.INSUFFICIENT_AMOUNT})
                transaction = Transactions(amount=post_transaction['amount'], sender_id=user_id,
                                           receiver_id=account.user_id,
                                           transaction_type_id=transaction_type.id)
                sender_acc.balance -= post_transaction['amount']
                account.balance += post_transaction['amount']
                db.session.add(transaction)
                db.session.commit()
                send_otp_email(transaction.id)
                return jsonify({'message': 'Transaction has been proceed..'})
            else:
                return jsonify({'message': constants.ACCOUNT_IS_NOT_EXIST})

        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def check_otp(transaction_id):
        otp_schema = OtpCheck(only=["otp", ])
        otp_data = request.get_json()
        try:
            otp_post_data = otp_schema.load(otp_data)
            otp_in_db = OtpByMail.query.filter_by(transaction_id=transaction_id).first()
            transaction = Transactions.query.filter_by(id=transaction_id).first()
            if transaction.is_transfer == 'Success':
                return jsonify({'message': 'Transaction for this transaction id is already done..'})
            if otp_in_db:
                if otp_in_db.otp == otp_post_data['otp']:
                    if transaction:
                        sender = Account.query.filter_by(user_id=transaction.sender_id).first()
                        receiver = Account.query.filter_by(user_id=transaction.receiver_id).first()
                        sender.balance -= transaction.amount
                        receiver.balance += transaction.amount
                        transaction.is_transfer = 'Success'
                        db.session.delete(otp_in_db)
                        db.session.commit()
                    return jsonify({'message': constants.TRANSACTION_DONE_SUCCESSFULLY})
                else:
                    db.session.delete(otp_in_db)
                    transaction.is_transfer = 'Fail'
                    db.session.commit()
                    return jsonify({'message': 'Transaction failed due to wrong otp'})
            else:
                return jsonify({'message': 'There is no OTP found for this user...'})

        except ValidationError as err:
            return jsonify(err.messages)


class PayBackService:

    @staticmethod
    def pay_loan():
        amount_schema = PayBack(only=["amount", "password"])
        json_data = request.get_json()
        try:
            post_data = amount_schema.load(json_data)
            loan = Loans.query.filter_by(user_id=get_jwt_identity()).first()
            user = User.query.filter_by(id=get_jwt_identity()).first()
            if not loan:
                return jsonify({'message': 'No loan found for this user...'})
            if loan.amount < post_data['amount']:
                return jsonify({'message': 'Your paying amount is greater than loan amount...'})

            user_acc = Account.query.filter_by(user_id=get_jwt_identity()).first()
            if user.password == post_data['password']:
                user_acc.balance -= post_data['amount']
                loan.amount -= post_data['amount']
                transaction_type = TransactionTypes.query.filter_by(type='Paid Loan').first()
                transaction = Transactions(amount=post_data['amount'],
                                           sender_id=user.id,
                                           receiver_id=user.id,
                                           transaction_type_id=transaction_type.id,
                                           is_transfer='Success')
                db.session.add(transaction)
                db.session.commit()
                return jsonify({'message': 'The loan amount has been paid successfully...'})
            else:
                return jsonify({'message': 'Password is wrong...Failed Transaction'})
        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def pay_insurance():
        amount_schema = PayBack(only=["amount", "password"])
        json_data = request.get_json()
        try:
            post_data = amount_schema.load(json_data)
            insurance = Insurances.query.filter_by(user_id=get_jwt_identity()).first()
            user = User.query.filter_by(id=get_jwt_identity()).first()
            if not insurance:
                return jsonify({'message': 'No insurance found for this user...'})
            # add this at the end for status validation for particular insurance [ mandatory part ]
            # if insurance.status == 'Inactive':
            #     return jsonify({'message': 'Insurance officer has not made this active insurance yet...'})
            # if insurance.claim_status == 'Claimed':
            #     return jsonify({'message': 'This insurance is not claimed yet...'})
            if insurance.amount < post_data['amount']:
                return jsonify({'message': 'Your paying amount is greater than insurance amount...'})
            user_acc = Account.query.filter_by(user_id=get_jwt_identity()).first()
            if user.password == post_data['password']:
                user_acc.balance -= post_data['amount']
                insurance.amount -= post_data['amount']
                transaction_type = TransactionTypes.query.filter_by(type='Paid Insurance').first()
                transaction = Transactions(amount=post_data['amount'],
                                           sender_id=user.id,
                                           receiver_id=user.id,
                                           transaction_type_id=transaction_type.id,
                                           is_transfer='Success')
                db.session.add(transaction)
                db.session.commit()
                return jsonify({'message': 'The insurance amount has been paid successfully...'})
            else:
                return jsonify({'message': 'Password is wrong...Failed Transaction'})
        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def transfer_to_saving():
        amount_schema = PayBack(only=["amount", "password"])
        json_data = request.get_json()
        try:
            post_data = amount_schema.load(json_data)
            user = User.query.filter_by(id=get_jwt_identity()).first()
            user_acc = Account.query.filter_by(user_id=get_jwt_identity()).first()
            if user.password == post_data['password']:
                if user_acc.balance < post_data['amount']:
                    return jsonify({'message': 'Insufficient balance to transact this process..'})
                user_acc.balance -= post_data['amount']
                user_acc.saving += post_data['amount']
                transaction_type = TransactionTypes.query.filter_by(type='Acc to Sav').first()
                transaction = Transactions(amount=post_data['amount'],
                                           sender_id=user.id,
                                           receiver_id=user.id,
                                           transaction_type_id=transaction_type.id,
                                           is_transfer='Success')
                db.session.add(transaction)
                db.session.commit()
                return jsonify({'message': 'The amount has been added to savings successfully...'})
            return jsonify({'message': 'Password is wrong...Failed Transaction'})
        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def transfer_to_account():
        amount_schema = PayBack(only=["amount", "password"])
        json_data = request.get_json()
        try:
            post_data = amount_schema.load(json_data)
            user = User.query.filter_by(id=get_jwt_identity()).first()
            user_acc = Account.query.filter_by(user_id=get_jwt_identity()).first()
            if user.password == post_data['password']:
                if user_acc.saving < post_data['amount']:
                    return jsonify({'message': 'Insufficient balance to transact this process..'})
                user_acc.saving -= post_data['amount']
                user_acc.balance += post_data['amount']
                transaction_type = TransactionTypes.query.filter_by(type='Sav to Acc').first()
                transaction = Transactions(amount=post_data['amount'],
                                           sender_id=user.id,
                                           receiver_id=user.id,
                                           transaction_type_id=transaction_type.id,
                                           is_transfer='Success')
                db.session.add(transaction)
                db.session.commit()
                return jsonify({'message': 'The amount has been added to main balance successfully...'})
            return jsonify({'message': 'Password is wrong...Failed Transaction'})
        except ValidationError as err:
            return jsonify(err.messages)
