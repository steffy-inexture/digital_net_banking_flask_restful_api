from flask import request, jsonify

from BS.User import constants
from BS.User.models import User
from BS.User.schemas import ParticularUserSchema


def get_particular_user_data(id):
    user_schema = ParticularUserSchema()
    user = User.query.filter_by(id=id).first()
    if not user:
        return jsonify(message=constants.USER_DOES_NOT_EXIST), 404

    json_user_detail = user_schema.dump(user)
    return jsonify(json_user_detail)
