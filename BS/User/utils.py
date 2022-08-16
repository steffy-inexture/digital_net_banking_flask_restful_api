from functools import wraps

from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from BS.User.models import User, UserRoles


def is_user():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user = User.query.filter_by(user_id=get_jwt_identity()).first()
            user_role = UserRoles.filter_by(id=user.user_role_id).first()
            if user_role.role == 'user':
                return fn(*args, **kwargs)
            else:
                return jsonify(message="Only user can access this page!"), 403

        return decorator

    return wrapper