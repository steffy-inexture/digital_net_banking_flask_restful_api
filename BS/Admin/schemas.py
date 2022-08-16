from marshmallow import post_load

from BS import ma
from BS.User.models import UserRoles, User


class AllUserRolesSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = UserRoles
        include_fk = True

    @post_load
    def make_object(self,data,**kwargs):
        return UserRoles(**data)

class UserDataSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        include_fk = True

    @post_load
    def make_object(self,data,**kwargs):
        return User(**data)