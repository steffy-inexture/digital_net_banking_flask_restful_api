# CRUD OPERATION FOR USER TYPES
from flask.views import MethodView
from flask_jwt_extended import jwt_required

from BS.Admin import services
from BS.User.utils import is_admin


class UserRolesData(MethodView):
    """
        ADMIN CAN GET ALL USER ROLES [ get request ]
        ADMIN CAN ADD NEW USER ROLE [ post request ]
        ADMIN CAN DELETE PARTICULAR USER ROLE [ delete request ]
    """
    decorators = [jwt_required(), is_admin()]
    user_roles_service_obj = services.UserRolesServices()

    @classmethod
    def get(cls):
        return cls.user_roles_service_obj.get_all_user_roles()

    @classmethod
    def post(cls):
        return cls.user_roles_service_obj.add_new_user_role()

    @classmethod
    def delete(cls, id):
        return cls.user_roles_service_obj.delete_existed_user_role(id)


class UserData(MethodView):
    """
        ADMIN CAN ADD THE NEW USER
        AND GIVE THEM RELEVANT USER AUTHORITY [ user role in our case ]
        SUCH AS User/Branch officer/Loan Officer/Insurance Officer
    """
    decorators = [jwt_required(), is_admin()]
    user_services_obj = services.UserServices()

    @classmethod
    def post(cls):
        return cls.user_services_obj.add_new_user()

    @classmethod
    def get(cls):
        return cls.user_services_obj.get_all_users()


class GetAllBranchOfficers(MethodView):
    """
        GET ALL BRANCH OFFICER'S DATA [ get request ]
    """
    decorators = [jwt_required(), is_admin()]
    branch_officers_obj = services.BankOfficersServices()

    @classmethod
    def get(cls):
        return cls.branch_officers_obj.get_all_branch_officers()

    @classmethod
    def delete(cls, id):
        return cls.branch_officers_obj.delete_existed_branch_officer(id)


class GetAllLoanOfficers(MethodView):
    """
        GET ALL LOAN OFFICER'S DATA [ get request ]
    """
    decorators = [jwt_required(), is_admin()]
    branch_officers_obj = services.BankOfficersServices()

    @classmethod
    def get(cls):
        return cls.branch_officers_obj.get_all_loan_officers()

    @classmethod
    def delete(cls, id):
        return cls.branch_officers_obj.delete_existed_loan_officer(id)


class GetAllInsuranceOfficers(MethodView):
    """
        GET ALL INSURANCE OFFICER'S DATA [ get request ]
    """
    decorators = [jwt_required(), is_admin()]
    branch_officers_obj = services.BankOfficersServices()

    @classmethod
    def get(cls):
        return cls.branch_officers_obj.get_all_insurance_officers()

    @classmethod
    def delete(cls, id):
        return cls.branch_officers_obj.delete_existed_insurance_officer(id)


class AccountTypeData(MethodView):
    decorators = [jwt_required(), is_admin()]
    account_type_service = services.AccountTypeServices()

    @classmethod
    def get(cls):
        return cls.account_type_service.get_all_account_types()

    @classmethod
    def post(cls):
        return cls.account_type_service.post_new_account_type()

    @classmethod
    def delete(cls, id):
        return cls.account_type_service.delete_specific_account_type(id)


class CardRequests(MethodView):
    decorators = [jwt_required(), is_admin()]
    card_req_service = services.CardsRequestsService()

    @classmethod
    def get(cls):
        return cls.card_req_service.get_all_card_requests()

    @classmethod
    def put(cls, id):
        return cls.card_req_service.give_approval_for_card(id)
