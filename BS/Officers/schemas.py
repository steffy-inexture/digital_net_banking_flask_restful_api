from marshmallow import post_load

from BS import ma
from BS.Officers.models import LoanTypes, InsuranceTypes


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
