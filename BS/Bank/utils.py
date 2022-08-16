from functools import wraps

from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

from BS.User.models import User


def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user = User.query.filter_by(user_id=get_jwt_identity()).first()
            if user.type_user == 'admin':
                return fn(*args, **kwargs)
            else:
                return jsonify(message="This page is accessible for admin only!"), 403

        return decorator

    return wrapper
