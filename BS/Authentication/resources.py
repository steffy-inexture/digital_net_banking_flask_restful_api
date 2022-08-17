from flask.views import MethodView

from BS.Authentication import services


class RegistrationAuth(MethodView):
    def post(self):
        return services.post_registration()

class LoginAuth(MethodView):
    def post(self):
        return services.post_login()