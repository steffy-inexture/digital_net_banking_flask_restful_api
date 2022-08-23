from flask.views import MethodView

from BS.Authentication import services


class RegistrationAuth(MethodView):
    registration_service = services.RegistrationService()

    @classmethod
    def post(cls):
        return cls.registration_service.post_registration()


class LoginAuth(MethodView):
    login_service = services.LoginService()

    @classmethod
    def post(cls):
        return cls.login_service.post_login()
