import datetime
import random

from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from sqlalchemy import func

from BS import db
from BS.Bank.models import Account, Cards
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

def post_card_request():
    current_user_id = get_jwt_identity()
    account = Account.query.filter_by(user_id=current_user_id).first()
    if account:
        card = Cards.query.filter_by(account_id=account.id).first()
        if card:
            return jsonify(message="User has already card"), 404
        else:
            card = db.session.query(func.max(Cards.number)).first()
            if card[0]:
                card_number = card[0] + 1
            else:
                card_number = 10000
            cvv_number = random.randint(111, 999)
            card_pin = random.randint(1111, 9999)
            expiry_date = datetime.datetime(2026, 7, 19, 12, 0, 0)
            card = Cards(
                number=card_number,
                cvv_number=cvv_number,
                card_pin=card_pin,
                expiry_date=expiry_date,
                account_id=account.id
            )
            db.session.add(card)
            db.session.commit()
            return jsonify(message="Card has been added successfully"), 404
    else:
        return jsonify(message="Account is not exist for this user..."), 404
