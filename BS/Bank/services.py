from flask import jsonify, request
from marshmallow import ValidationError
from sqlalchemy import func

from BS import db
from BS.Bank.models import Bank, Atm, Branches, Account, AccountType
from BS.Bank.schemas import BankDetailSchema, AtmDetailSchema, UpdateAtmDetailSchema, BranchDetailSchema, \
    UpdateBranchDetailSchema
from BS.Bank import constants
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
