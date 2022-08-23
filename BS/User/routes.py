from flask import Blueprint

from BS.User.resources import UserRegisteration, ParticularUser, CardRequest

user = Blueprint('user', __name__)

user.add_url_rule('/register_user', view_func=UserRegisteration.as_view('user_registration'))
user.add_url_rule('/get_user/<int:id>', view_func=ParticularUser.as_view('particular_user'))

# card request [ post request ]
user.add_url_rule('/card_request', view_func=CardRequest.as_view('card_request'))
