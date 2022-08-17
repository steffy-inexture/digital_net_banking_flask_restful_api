from flask import Blueprint

from BS.Authentication.resources import LoginAuth, RegistrationAuth

auth = Blueprint('auth', __name__)

auth.add_url_rule('/login', view_func=LoginAuth.as_view('login'))
auth.add_url_rule('/reg', view_func=RegistrationAuth.as_view('register'))