from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from marshmallow import ValidationError

from BS import db
from BS.Authentication import constants
from BS.Authentication.schemas import UserDataReg, LoginUserSchema
from BS.User.models import User


def post_registration():
    post_new_user_schema = UserDataReg()
    new_user_data = request.get_json()
    try:
        existed_user_name = User.query.filter_by(user_name=new_user_data['user_name']).first()
        if existed_user_name:
            return jsonify({'message': constants.USER_NAME_ALREADY_EXISTED})
        else:
            existed_email = User.query.filter_by(email=new_user_data['email']).first()
            if existed_email:
                return jsonify({'message': constants.USER_EMAIL_ALREADY_EXISTED})
            else:
                new_post_user = post_new_user_schema.load(new_user_data)
                db.session.add(new_post_user)
                db.session.commit()
                return jsonify({'message': constants.REGISTRATION_SUCCESSFULL})

    except ValidationError as err:
        return jsonify(err.messages)

def post_login():
    login_schema = LoginUserSchema()
    user_data = request.get_json()
    try:
        login_user = login_schema.load(user_data)
        user_detail = User.query.filter_by(email=login_user['email']).first()
        access_token = create_access_token(identity=user_detail.id)
        refresh_token = create_refresh_token(identity=user_detail.id)
        return jsonify({'token': {'access_token': access_token, 'refresh_token': refresh_token},
                        'message': 'Login Successfully'}), 200

    except ValidationError as err:
        return jsonify(err.messages), 401
