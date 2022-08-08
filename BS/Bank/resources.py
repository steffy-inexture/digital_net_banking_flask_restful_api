from flask.views import MethodView
from BS.Bank import services


class BankDetail(MethodView):
    """
        Bank table's GET & POST methods
    """

    def get(self):
        return services.get_bank_details()

    def post(self):
        return services.post_bank_details()

class AtmDetail(MethodView):
    """
        Atm table's GET ALL ATM & POST Atm methods
    """

    def get(self):
        return services.get_all_atm_data()

class ParticularAtm(MethodView):
    """
        Particular one atm's GET, PUT & DELETE Methods
    """

    def get(self,id):
        return services.get_particular_atm(id)

    def post(self):
        return services.post_atm_data()

    def delete(self, id):
        return services.delete_particular_atm(id)

    def put(self, id):
        return services.put_particular_atm(id)

class AllBranchesData(MethodView):
    """
        For all branches data
    """
    def get(self):
        return services.get_all_branches_data()


class ParticularBranches(MethodView):
    """
        Particular one branch's GET, PUT & DELETE Methods
    """

    def get(self,id):
        return services.get_particular_branch(id)

    def post(self):
        return services.post_branch_data()

    def delete(self, id):
        return services.delete_particular_branch(id)

    def put(self, id):
        return services.put_particular_branch(id)

