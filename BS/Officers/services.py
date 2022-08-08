from flask import jsonify, request
from marshmallow import ValidationError

from BS import db
from BS.Officers import constants
from BS.Officers.models import LoanTypes, InsuranceTypes
from BS.Officers.schemas import LoanTypeSchema, UpdateLoanTypeDetailSchema, InsuranceTypeSchema, \
    UpdateInsuranceTypeDetailSchema


# loan officer's work starts here

def get_all_loan_types():
    loan_type_schema = LoanTypeSchema(many=True)
    loan_type_detail = LoanTypes.query.all()
    json_loan_types_detail = loan_type_schema.dump(loan_type_detail)
    return jsonify(json_loan_types_detail)


def get_particular_loan_type(id):
    loan_type_schema = LoanTypeSchema()
    loan_type_data = LoanTypes.query.filter_by(id=id).first()
    if loan_type_data:
        json_loan_type_detail = loan_type_schema.dump(loan_type_data)
        return jsonify(json_loan_type_detail)
    else:
        return jsonify(message=constants.LOAN_TYPE_DOES_NOT_EXIST), 404


def post_particular_loan_type():
    loan_type_schema = LoanTypeSchema()
    loan_type_data = request.get_json()
    try:
        existed_loan_type_name = LoanTypes.query.filter_by(name=loan_type_data['name']).first()
        if existed_loan_type_name:
            return jsonify({'message': constants.LOAN_TYPE_ALREADY_EXIST})
        else:
            loan_type_post_data = loan_type_schema.load(loan_type_data)
            db.session.add(loan_type_post_data)
            db.session.commit()
            return jsonify({'message': constants.LOAN_TYPE_ADDED})

    except ValidationError as err:
        return jsonify(err.messages)


# add validation for weather this loan type has allocated with some user or not afterwords [ NEEDED MODIFICATION ]
def delete_particular_loan_type(id):
    delete_loan_type = LoanTypes.query.filter_by(id=id).first()
    if delete_loan_type:
        db.session.delete(delete_loan_type)
        db.session.commit()
        return jsonify(message=constants.LOAN_TYPE_DELETED), 200
    else:
        return jsonify(message=constants.LOAN_TYPE_DOES_NOT_EXIST), 404


# add validation for weather this branch has allocated with some user or not afterwords [ NEEDED MODIFICATION ]
def put_particular_loan_type(id):
    loan_type_schema = UpdateLoanTypeDetailSchema(only="name" and "rate_interest")
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

def get_all_insurance_types():
    insurance_type_schema = InsuranceTypeSchema(many=True)
    insurance_type_detail = InsuranceTypes.query.all()
    json_insurance_types_detail = insurance_type_schema.dump(insurance_type_detail)
    return jsonify(json_insurance_types_detail)


def get_particular_insurance_type(id):
    insurance_type_schema = InsuranceTypeSchema()
    insurance_type_data = InsuranceTypes.query.filter_by(id=id).first()
    if insurance_type_data:
        json_insurance_type_detail = insurance_type_schema.dump(insurance_type_data)
        return jsonify(json_insurance_type_detail)
    else:
        return jsonify(message=constants.INSURANCE_TYPE_DOES_NOT_EXIST), 404


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


# add validation for weather this loan type has allocated with some user or not afterwords [ NEEDED MODIFICATION ]
def delete_particular_insurance_type(id):
    delete_insurance_type = InsuranceTypes.query.filter_by(id=id).first()
    if delete_insurance_type:
        db.session.delete(delete_insurance_type)
        db.session.commit()
        return jsonify(message=constants.INSURANCE_TYPE_DELETED), 200
    else:
        return jsonify(message=constants.INSURANCE_TYPE_DOES_NOT_EXIST), 404


# add validation for weather this branch has allocated with some user or not afterwords [ NEEDED MODIFICATION ]
def put_particular_insurance_type(id):
    insurance_type_schema = UpdateInsuranceTypeDetailSchema(only="name" and "monthly_pay")
    insurance_type_data = request.get_json()
    insurance_type = InsuranceTypes.query.filter_by(id=id).first()
    try:
        insurance_type_schema.load(insurance_type_data, instance=insurance_type)
        db.session.commit()
        return jsonify({'message': constants.INSURANCE_TYPE_UPDATED})

    except ValidationError as err:
        return jsonify(err.messages)

# insurance officer's work ends here
