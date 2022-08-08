from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError

from BS import db
from BS.User.schema import RegisterStaffSchema


class RegisterStaff(MethodView):

    def post(self):
        register_staff_schema = RegisterStaffSchema()
        staff_data = request.get_json()
        try:
            staff_register = register_staff_schema.load(staff_data)
            print(staff_register)
            db.session.add(staff_register)
            db.session.commit()
            return jsonify({'message': 'Staff Created'})

        except ValidationError as err:
            return jsonify(err.messages)




