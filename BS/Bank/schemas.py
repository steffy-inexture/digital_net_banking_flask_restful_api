from flask_jwt_extended import get_jwt_identity
from flask_marshmallow import fields
from marshmallow import post_load, validates_schema, ValidationError

from BS.factory import ma
from BS.Bank.models import Bank, Atm, Branches, LoanTypes, InsuranceTypes, Transactions, Account, OtpByMail


class BankDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bank

    @post_load
    def make_object(self, data, **kwargs):
        return Bank(**data)


class AtmDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Atm

    @post_load
    def make_object(self, data, **kwargs):
        return Atm(**data)


class UpdateAtmDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Atm
        load_instance = True


class BranchDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Branches

    @post_load
    def make_object(self, data, **kwargs):
        return Branches(**data)


class UpdateBranchDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Branches
        load_instance = True


class LoanRequestSchema(ma.SQLAlchemyAutoSchema):
    loan_id = fields.fields.Int(required=True)
    amount = fields.fields.Int(required=True)

    @validates_schema
    def validate_loan_id(self, data, **kwargs):
        available_loans = LoanTypes.query.filter_by(id=data['loan_id']).first()
        errors = {}
        if not available_loans:
            errors['loan_is_not_exist'] = ['Loan is not existed!']
        if errors:
            raise ValidationError(errors)

class InsuranceRequestSchema(ma.SQLAlchemyAutoSchema):
    insurance_id = fields.fields.Int(required=True)
    amount = fields.fields.Int(required=True)

    @validates_schema
    def validate_insurance_id(self, data, **kwargs):
        available_insurance = InsuranceTypes.query.filter_by(id=data['insurance_id']).first()
        errors = {}
        if not available_insurance:
            errors['insurance_is_not_exist'] = ['Insurance is not existed!']
        if errors:
            raise ValidationError(errors)


class TransactMoneySchema(ma.SQLAlchemyAutoSchema):
    number = fields.fields.Int(required=True)
    amount = fields.fields.Int(required=True)

    @validates_schema
    def validate_acc_number(self,data, **kwargs):
        errors = {}
        account = Account.query.filter_by(number=data['number']).first()
        if not account:
            errors['account_is_not_exist'] = ['Desired account is not exist..!']
        if errors:
            raise ValidationError(errors)


class OtpCheck(ma.SQLAlchemyAutoSchema):
    otp = fields.fields.Int(required=True)

    @validates_schema
    def validate_otp(self, data, **kwargs):
        errors = {}
        user_id = get_jwt_identity()
        otp_data = OtpByMail.query.filter_by(sender_id=user_id).first()
        if not otp_data:
            errors['otp_is_not_exist'] = ['There is no OTP for this user..!']
        if errors:
            raise ValidationError(errors)

class PayBack(ma.SQLAlchemyAutoSchema):
    amount = fields.fields.Int(required=True)
    password = fields.fields.String(required=True)

