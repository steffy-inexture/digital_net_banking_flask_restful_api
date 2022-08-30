from marshmallow import post_load

from BS.factory import ma
from BS.Bank.models import AccountType, Cards
from BS.User.models import UserRoles, User


class AllUserRolesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UserRoles
        ordered = True
        include_fk = True

    @post_load
    def make_object(self, data, **kwargs):
        return UserRoles(**data)


class UserDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        ordered = True
        include_fk = True

    @post_load
    def make_object(self, data, **kwargs):
        return User(**data)


class AccountTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AccountType

    @post_load
    def make_object(self, data, **kwargs):
        return AccountType(**data)


class CardRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cards
        load_instance = True
        exclude = ('card_pin','creation_date','cvv_number','expiry_date')

    @post_load
    def make_object(self, data, **kwargs):
        return AccountType(**data)

class StatusCardRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cards
        load_instance = True

