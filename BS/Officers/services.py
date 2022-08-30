from flask import jsonify, request
from marshmallow import ValidationError

from BS.factory import db
from BS.Bank.models import LoanTypes, InsuranceTypes, Loans, Insurances, Account
from BS.Officers import constants
from BS.Officers.schemas import LoanTypeSchema, UpdateLoanTypeDetailSchema, InsuranceTypeSchema, \
    UpdateInsuranceTypeDetailSchema, LoanDetailSchema, UpdateLoanSchema, InsuranceDetailSchema, UpdateInsuranceSchema


# loan officer's work starts here
class LoanOfficerservices:
    @staticmethod
    def get_all_loan_types():
        loan_type_schema = LoanTypeSchema(many=True)
        loan_type_detail = LoanTypes.query.all()
        json_loan_types_detail = loan_type_schema.dump(loan_type_detail)
        return jsonify(json_loan_types_detail)

    @staticmethod
    def get_particular_loan_type(id):
        loan_type_schema = LoanTypeSchema()
        loan_type_data = LoanTypes.query.filter_by(id=id).first()
        if loan_type_data:
            json_loan_type_detail = loan_type_schema.dump(loan_type_data)
            return jsonify(json_loan_type_detail)
        else:
            return jsonify(message=constants.LOAN_TYPE_DOES_NOT_EXIST), 404

    @staticmethod
    def post_particular_loan_type():
        loan_type_schema = LoanTypeSchema()
        loan_type_data = request.get_json()
        try:
            existed_loan_type_name = LoanTypes.query.filter_by(type_for_loan=loan_type_data['type_for_loan']).first()
            if existed_loan_type_name:
                return jsonify({'message': constants.LOAN_TYPE_ALREADY_EXIST})
            else:
                loan_type_post_data = loan_type_schema.load(loan_type_data)
                db.session.add(loan_type_post_data)
                db.session.commit()
                return jsonify({'message': constants.LOAN_TYPE_ADDED})

        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def delete_particular_loan_type(id):
        delete_loan_type = LoanTypes.query.filter_by(id=id).first()
        if delete_loan_type:
            loan_type_is_occupied = Loans.query.filter_by(loan_type_id=id).first()
            if not loan_type_is_occupied:
                db.session.delete(delete_loan_type)
                db.session.commit()
                return jsonify(message=constants.LOAN_TYPE_DELETED), 200
            return jsonify(message=constants.LOAN_TYPE_IS_OCCUPIED), 404
        else:
            return jsonify(message=constants.LOAN_TYPE_DOES_NOT_EXIST), 404

    # add validation for weather this branch has allocated with some user or not afterwords [ NEEDED MODIFICATION ]
    @staticmethod
    def put_particular_loan_type(id):
        is_loan_type_exist = LoanTypes.query.filter_by(id=id).first()
        if not is_loan_type_exist:
            return jsonify({'message': constants.LOAN_TYPE_IS_NOT_EXISTED})
        loan_type_schema = UpdateLoanTypeDetailSchema(only=['rate_interest'])
        loan_type_data = request.get_json()
        loan_type = LoanTypes.query.filter_by(id=id).first()
        try:
            loan_type_schema.load(loan_type_data, instance=loan_type)
            db.session.commit()
            return jsonify({'message': constants.LOAN_TYPE_UPDATED})
        except ValidationError as err:
            return jsonify(err.messages)


# loan officer's work ends here

# ----------------------------------------------------------------------------------------------------

# insurance officer's work starts here
class InsuranceServices:

    @staticmethod
    def get_all_insurance_types():
        insurance_type_schema = InsuranceTypeSchema(many=True)
        insurance_type_detail = InsuranceTypes.query.all()
        json_insurance_types_detail = insurance_type_schema.dump(insurance_type_detail)
        return jsonify(json_insurance_types_detail)

    @staticmethod
    def get_particular_insurance_type(id):
        insurance_type_schema = InsuranceTypeSchema()
        insurance_type_data = InsuranceTypes.query.filter_by(id=id).first()
        if insurance_type_data:
            json_insurance_type_detail = insurance_type_schema.dump(insurance_type_data)
            return jsonify(json_insurance_type_detail)
        else:
            return jsonify(message=constants.INSURANCE_TYPE_DOES_NOT_EXIST), 404

    @staticmethod
    def post_particular_insurance_type():
        insurance_type_schema = InsuranceTypeSchema()
        insurance_type_data = request.get_json()
        try:
            existed_insurance_type_name = InsuranceTypes.query.filter_by(name=insurance_type_data['name']).first()
            if existed_insurance_type_name:
                return jsonify({'message': constants.INSURANCE_TYPE_ALREADY_EXIST})
            else:
                insurance_type_post_data = insurance_type_schema.load(insurance_type_data)
                db.session.add(insurance_type_post_data)
                db.session.commit()
                return jsonify({'message': constants.INSURANCE_TYPE_ADDED})

        except ValidationError as err:
            return jsonify(err.messages)

    @staticmethod
    def delete_particular_insurance_type(id):
        delete_insurance_type = InsuranceTypes.query.filter_by(id=id).first()
        if delete_insurance_type:
            is_insurance_occupied = Insurances.query.filter_by(insurance_type_id=id).first()
            if not is_insurance_occupied:
                db.session.delete(delete_insurance_type)
                db.session.commit()
                return jsonify(message=constants.INSURANCE_TYPE_DELETED), 200
            return jsonify(message=constants.INSURANCE_TYPE_IS_OCCUPIED), 404
        return jsonify(message=constants.INSURANCE_TYPE_DOES_NOT_EXIST), 404

    # add validation for weather this branch has allocated with some user or not afterwords [ NEEDED MODIFICATION ]
    @staticmethod
    def put_particular_insurance_type(id):
        insurance_type_schema = UpdateInsuranceTypeDetailSchema(only=["monthly_pay"])
        insurance_type_data = request.get_json()
        insurance_type = InsuranceTypes.query.filter_by(id=id).first()
        if not insurance_type:
            return jsonify({'message': constants.INSURANCE_TYPE_IS_NOT_EXISTED})

        try:
            insurance_type_schema.load(insurance_type_data, instance=insurance_type)
            db.session.commit()
            return jsonify({'message': constants.INSURANCE_TYPE_UPDATED})

        except ValidationError as err:
            return jsonify(err.messages)


# insurance officer's work ends here

class LoanRequestsServices:

    @staticmethod
    def get_all_loan_requests():
        loan_req_schema = LoanDetailSchema(many=True)
        loan_detail = Loans.query.all()
        json_loan_data = loan_req_schema.dump(loan_detail)
        return jsonify(json_loan_data)

    @staticmethod
    def approval_for_loan(id):
        update_loan_schema = UpdateLoanSchema(only=['status'])
        loan_status_data = request.get_json()
        is_loan_exist = Loans.query.filter_by(id=id).first()
        if not is_loan_exist:
            return jsonify({'message': constants.THIS_USER_HAS_NO_LOAN})
        try:
            if loan_status_data['status'] == is_loan_exist.status:
                return jsonify({'message': constants.STATUS_IS_ALREADY_ACTIVATED})
            update_loan_schema.load(loan_status_data, instance=is_loan_exist)
            account = Account.query.filter_by(user_id=is_loan_exist.user_id).first()
            if loan_status_data['status'] == 'Active':
                account.balance += is_loan_exist.amount
            db.session.commit()
            return jsonify({'message': constants.LOAN_STATUS_UPDATED})
        except ValidationError as err:
            return jsonify(err.messages)


class InsuranceRequestsServices:

    @staticmethod
    def get_all_insurance_requests():
        insurance_req_schema = InsuranceDetailSchema(many=True)
        insurance_detail = Insurances.query.all()
        json_insurance_data = insurance_req_schema.dump(insurance_detail)
        return jsonify(json_insurance_data)

    @staticmethod
    def approval_for_insurance(id):
        update_insurance_schema = UpdateInsuranceSchema(only=['status'])
        insurance_status_data = request.get_json()
        is_insurance_exist = Insurances.query.filter_by(id=id).first()
        if not is_insurance_exist:
            return jsonify({'message': constants.THIS_USER_HAS_NO_INSURANCE})
        try:
            if insurance_status_data['status'] == is_insurance_exist.status:
                return jsonify({'message': constants.STATUS_IS_ALREADY_ACTIVATED})
            update_insurance_schema.load(insurance_status_data, instance=is_insurance_exist)
            db.session.commit()
            return jsonify({'message': constants.INSURANCE_STATUS_UPDATED})
        except ValidationError as err:
            return jsonify(err.messages)
