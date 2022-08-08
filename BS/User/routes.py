from flask import Blueprint

from BS.User.resources import RegisterStaff

user = Blueprint('user', __name__)

user.add_url_rule('/register_user', view_func=RegisterStaff.as_view('register_staff'))