from marshmallow import post_load

from BS import ma
from BS.Bank.models import Bank, Atm, Branches


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


