from marshmallow import fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from BS import ma
from BS.User.models import User


# KEEP THIS IN MIND THIS IS HOW WE CAN USER FK AND RELATION [ Refer User and UserRoles Table ]
# user = User.query.filter_by(id=4).first()
# print(f"***************** {user.user_roles.role}")


class RegisterUserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        include_fk = True

    @post_load
    def make_object(self,data,**kwargs):
        return User(**data)

class ParticularUserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        include_fk = True

    @post_load
    def make_object(self,data,**kwargs):
        return User(**data)




