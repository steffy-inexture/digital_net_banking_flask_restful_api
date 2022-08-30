from flask import request, jsonify
from flask.views import MethodView
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError

from BS.factory import db
from BS.User import services
from BS.User.schemas import RegisterUserSchema, ParticularUserSchema


class UserRegisteration(MethodView):

    def post(self):
        register_user_schema = RegisterUserSchema()
        user_data = request.get_json()
        try:
            user_register = register_user_schema.load(user_data)
            db.session.add(user_register)
            db.session.commit()
            return jsonify({'message': 'New User has been Created'})

        except ValidationError as err:
            return jsonify(err.messages)


class ParticularUser(MethodView):
    decorators = [jwt_required()]

    def get(self, id):
        return services.get_particular_user_data(id)

class UserRolesView(MethodView):

    def get(self):
        pass

    def put(self,id):
        pass

    def post(self):
        pass

    def delete(self,id):
        pass

class GetUserRoleById(MethodView):

    def get(self,id):
        pass


class CardRequest(MethodView):
    decorators = [jwt_required()]

    def post(self):
        return services.post_card_request()