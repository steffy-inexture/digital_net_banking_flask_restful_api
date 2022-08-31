from marshmallow import post_load, ValidationError, validates_schema, fields

from BS import ma
from BS.User.models import User


class UserDataReg(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True

    @post_load
    def make_object(self, data, **kwargs):
        return User(**data)

    @validates_schema
    def validate_user(self, data, **kwargs):
        errors = {}

        if len(data['user_name']) < 2:
            errors['length_user_name'] = ['User name must be at least 2 characters long!']
        if errors:
            raise ValidationError(errors)


class LoginUserSchema(ma.SQLAlchemyAutoSchema):
    email = fields.String(required=True)
    password = fields.String(required=True)

    @post_load
    def make_object(self, data, **kwargs):
        return data

    @validates_schema
    def validate_user(self, data, **kwargs):
        errors = {}
        user_exists = User.query.filter_by(email=data['email']).first()
        if user_exists:
            if user_exists.password != data['password']:
                errors['password'] = ['Wrong Password!']
        if not user_exists:
            errors['email'] = ['Account Does Not Exist!']
        if errors:
            raise ValidationError(errors)
