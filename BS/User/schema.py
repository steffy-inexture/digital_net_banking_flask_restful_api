from marshmallow import fields, post_load

from BS import ma
from BS.User.models import User


# class UserSchema(ma.SQLAlchemyAutoSchema):
#
#     user_name = fields.String(required=True, )
#     user_dob = fields.String(required=True, )
#     user_address = fields.String(required=True, )
#     user_password = fields.String(required=True, )
#
#     class Meta:
#         model = User

class RegisterStaffSchema(ma.SQLAlchemyAutoSchema):
    # user = fields.Nested(UserSchema)

    class Meta:
        model = User
        # include_fk = True

    @post_load
    def make_object(self,data,**kwargs):
        return User(**data)
