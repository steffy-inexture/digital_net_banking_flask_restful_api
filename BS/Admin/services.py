# get all user roles from the 'UserRoles' table which is in user-->models.py
from flask import jsonify, request
from marshmallow import ValidationError

from BS import db
from BS.Admin import constants
from BS.Admin.schemas import AllUserRolesSchema, UserDataSchema, AccountTypeSchema, CardRequestSchema, \
    StatusCardRequestSchema
from BS.Bank.models import AccountType, Account, Cards
from BS.User.models import UserRoles, User


#  --------- for user role services GET/POST/DELETE starts
class UserRolesServices:

    @staticmethod
    def get_all_user_roles():
        get_all_user_role_schema = AllUserRolesSchema(many=True)
        user_roles = UserRoles.query.all()

        json_user_roles_detail = get_all_user_role_schema.dump(user_roles)
        return jsonify(json_user_roles_detail)

    @staticmethod
    def add_new_user_role():
        post_new_user_role_schema = AllUserRolesSchema()
        new_user_role_data = request.get_json()
        try:
            existed_role = UserRoles.query.filter_by(role=new_user_role_data['role']).first()
            if existed_role:
                return jsonify({'message': constants.USER_ROLE_ALREADY_EXISTED})
            else:
                new_post_user = post_new_user_role_schema.load(new_user_role_data)
                db.session.add(new_post_user)
                db.session.commit()
                return jsonify({'message': constants.NEW_USER_ROLE_ADDED})

        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def delete_existed_user_role(id):
        delete_user_role = UserRoles.query.filter_by(id=id).first()
        if not delete_user_role:
            return jsonify(message=constants.USER_ROLE_DOES_NOT_EXIST), 404
        else:
            user = User.query.filter_by(user_role_id=id).first()
            if not user:
                db.session.delete(delete_user_role)
                db.session.commit()
                return jsonify(message=constants.USER_ROLE_DELETED), 200
            else:
                return jsonify(message=constants.USER_ROLE_OCCUPIES_BY_USER), 404


#  --------- for user role services GET/POST/DELETE ends

#  --------- for user services /POST/ starts
class UserServices:
    @staticmethod
    def add_new_user():
        post_new_user_schema = UserDataSchema()
        new_user_data = request.get_json()
        try:
            existed_user_name = User.query.filter_by(user_name=new_user_data['user_name']).first()
            if existed_user_name:
                return jsonify({'message': constants.USER_NAME_ALREADY_EXISTED})
            else:
                existed_email = User.query.filter_by(email=new_user_data['email']).first()
                if existed_email:
                    return jsonify({'message': constants.USER_EMAIL_ALREADY_EXISTED})
                else:
                    new_post_user_role = post_new_user_schema.load(new_user_data)
                    db.session.add(new_post_user_role)
                    db.session.commit()
                    return jsonify({'message': constants.NEW_USER_ADDED})

        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def get_all_users():
        get_all_user_schema = UserDataSchema(many=True)
        users = User.query.all()

        json_user_detail = get_all_user_schema.dump(users)
        return jsonify(json_user_detail)


class BankOfficersServices:
    @staticmethod
    def get_all_branch_officers():
        branch_officer_role = UserRoles.query.filter_by(role="branch officer").first()
        get_all_branch_officer_schema = UserDataSchema(many=True)
        branch_officers = User.query.filter_by(user_role_id=branch_officer_role.id).all()
        json_branch_officers_detail = get_all_branch_officer_schema.dump(branch_officers)
        return jsonify(json_branch_officers_detail)

    @staticmethod
    def delete_existed_branch_officer(id):
        delete_branch_officer = User.query.filter_by(id=id).first()
        if not delete_branch_officer:
            return jsonify(message=constants.USER_DOES_NOT_EXIST), 404
        else:
            role = UserRoles.query.filter_by(role="branch officer").first()
            if delete_branch_officer.user_role_id != role.id:
                return jsonify(message=constants.USER_IS_NOT_BRANCH_OFFICER), 404
            else:
                db.session.delete(delete_branch_officer)
                db.session.commit()
                return jsonify(message=constants.BRANCH_OFFICER_DELETED), 200

    @staticmethod
    def get_all_loan_officers():
        loan_officer_role = UserRoles.query.filter_by(role="loan officer").first()
        get_all_loan_officer_schema = UserDataSchema(many=True)
        loan_officers = User.query.filter_by(user_role_id=loan_officer_role.id).all()
        json_loan_officers_detail = get_all_loan_officer_schema.dump(loan_officers)
        return jsonify(json_loan_officers_detail)

    @staticmethod
    def delete_existed_loan_officer(id):
        delete_loan_officer = User.query.filter_by(id=id).first()
        if not delete_loan_officer:
            return jsonify(message=constants.USER_DOES_NOT_EXIST), 404
        else:
            role = UserRoles.query.filter_by(role="loan officer").first()
            if delete_loan_officer.user_role_id != role.id:
                return jsonify(message=constants.USER_IS_NOT_LOAN_OFFICER), 404
            else:
                db.session.delete(delete_loan_officer)
                db.session.commit()
                return jsonify(message=constants.LOAN_OFFICER_DELETED), 200

    @staticmethod
    def get_all_insurance_officers():
        insurance_officer_role = UserRoles.query.filter_by(role="insurance officer").first()
        get_all_insurance_officer_schema = UserDataSchema(many=True)
        insurance_officers = User.query.filter_by(user_role_id=insurance_officer_role.id).all()
        json_insurance_officers_detail = get_all_insurance_officer_schema.dump(insurance_officers)
        return jsonify(json_insurance_officers_detail)

    @staticmethod
    def delete_existed_insurance_officer(id):
        delete_insurance_officer = User.query.filter_by(id=id).first()
        if not delete_insurance_officer:
            return jsonify(message=constants.USER_DOES_NOT_EXIST), 404
        else:
            role = UserRoles.query.filter_by(role="insurance officer").first()
            if delete_insurance_officer.user_role_id != role.id:
                return jsonify(message=constants.USER_IS_NOT_INSURANCE_OFFICER), 404
            else:
                db.session.delete(delete_insurance_officer)
                db.session.commit()
                return jsonify(message=constants.INSURANCE_OFFICER_DELETED), 200


#  --------- for user role services /POST/ ends

class AccountTypeServices:
    @staticmethod
    def get_all_account_types():
        get_all_ac_type_schema = AccountTypeSchema(many=True)
        acc_types = AccountType.query.all()
        json_acc_types_detail = get_all_ac_type_schema.dump(acc_types)
        return jsonify(json_acc_types_detail)

    @staticmethod
    def post_new_account_type():
        post_new_acc_type = AccountTypeSchema()
        new_data = request.get_json()
        try:
            existed_type = AccountType.query.filter_by(type=new_data['type']).first()
            if existed_type:
                return jsonify({'message': constants.ACCOUNT_TYPE_ALREADY_EXISTED})
            else:
                new_post_acc_type = post_new_acc_type.load(new_data)
                db.session.add(new_post_acc_type)
                db.session.commit()
                return jsonify({'message': constants.NEW_ACC_TYPE_ADDED})

        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def delete_specific_account_type(id):
        delete_acc_type = AccountType.query.filter_by(id=id).first()
        if not delete_acc_type:
            return jsonify(message=constants.ACC_TYPE_DOES_NOT_EXIST), 404
        else:
            user_occupied_with_type = Account.query.filter_by(type_id=id).first()
            if user_occupied_with_type:
                return jsonify(message=constants.USER_OCCUPIED_THIS_TYPE), 404
            else:
                db.session.delete(delete_acc_type)
                db.session.commit()
                return jsonify(message=constants.ACC_TYPE_DELETED), 200

class CardsRequestsService:

    @staticmethod
    def get_all_card_requests():
        get_all_cards_schema = CardRequestSchema(many=True)
        card_data = Cards.query.all()
        json_card_detail = get_all_cards_schema.dump(card_data)
        return jsonify(json_card_detail)

    @staticmethod
    def give_approval_for_card(id):
        card_schema = StatusCardRequestSchema(only=["is_active"])
        card_data = request.get_json()
        card = Cards.query.filter_by(id=id).first()
        if card:
            try:
                card_schema.load(card_data, instance=card)
                db.session.commit()
                if card_data['is_active'] == 'Active':
                    return jsonify({'message': constants.CARD_ACTIVATED}), 200
                return jsonify({'message': constants.CARD_DEACTIVATED}), 200
            except ValidationError as err:
                return jsonify(err.messages)
        else:
            return jsonify({'message': constants.CARD_DATA_IS_NOT_EXISTED}), 404