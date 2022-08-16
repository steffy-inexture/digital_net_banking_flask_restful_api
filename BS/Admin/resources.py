# CRUD OPERATION FOR USER TYPES
from flask.views import MethodView

from BS.Admin import services


class UserRolesData(MethodView):
    """
        ADMIN CAN GET ALL USER ROLES [ get request ]
        ADMIN CAN ADD NEW USER ROLE [ post request ]
        ADMIN CAN DELETE PARTICULAR USER ROLE [ delete request ]
    """

    def get(self):
        return services.get_all_user_roles()

    def post(self):
        return services.add_new_user_role()

    def delete(self, id):
        return services.delete_existed_user_role(id)


class UserData(MethodView):
    """
        ADMIN CAN ADD THE NEW USER
        AND GIVE THEM RELEVANT USER AUTHORITY [ user role in our case ]
        SUCH AS User/Branch officer/Loan Officer/Insurance Officer
    """                                                                                                                                                                                                     

    def post(self):
        return services.add_new_user()

    def get(self):
        return services.get_all_users()


class GetAllBranchOfficers(MethodView):
    """
        GET ALL BRANCH OFFICER'S DATA [ get request ]
    """

    def get(self):
        return services.get_all_branch_officers()

    def delete(self,id):
      return services.delete_existed_branch_officer(id)


class GetAllLoanOfficers(MethodView):
    """
        GET ALL LOAN OFFICER'S DATA [ get request ]
    """

    def get(self):
        return services.get_all_loan_officers()

    def delete(self,id):
      return services.delete_existed_loan_officer(id)


class GetAllInsuranceOfficers(MethodView):
    """
        GET ALL INSURANCE OFFICER'S DATA [ get request ]
    """

    def get(self):
        return services.get_all_insurance_officers()

    def delete(self,id):
      return services.delete_existed_insurance_officer(id)
