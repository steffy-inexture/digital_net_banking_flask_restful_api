from marshmallow import post_load

from BS.factory import ma
from BS.Bank.models import LoanTypes, InsuranceTypes, Loans, Insurances


# schema for loan types starts

class LoanTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LoanTypes

    @post_load
    def make_object(self, data, **kwargs):
        return LoanTypes(**data)


class UpdateLoanTypeDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LoanTypes
        load_instance = True


# schema for loan types ends

# schema for insurance types starts

class InsuranceTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InsuranceTypes

    @post_load
    def make_object(self, data, **kwargs):
        return InsuranceTypes(**data)


class UpdateInsuranceTypeDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = InsuranceTypes
        load_instance = True


# schema for loan types ends
class LoanDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Loans
        include_fk = True

    @post_load
    def make_object(self, data, **kwargs):
        return Loans(**data)


class UpdateLoanSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Loans
        include_fk = True
        load_instance=True


class InsuranceDetailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Insurances
        include_fk = True

    @post_load
    def make_object(self, data, **kwargs):
        return Insurances(**data)


class UpdateInsuranceSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Insurances
        include_fk = True
        load_instance=True


