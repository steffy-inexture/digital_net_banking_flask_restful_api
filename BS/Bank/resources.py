from flask.views import MethodView
from BS.Bank import services


class BankDetail(MethodView):
    bank_service = services.BankDetailServices()

    @classmethod
    def get(cls):
        return cls.bank_service.get_bank_details()

    @classmethod
    def post(cls):
        return cls.bank_service.post_bank_details()


class AtmDetail(MethodView):
    all_atm_service = services.AllAtmService()

    @classmethod
    def get(cls):
        return cls.all_atm_service.get_all_atm_data()


class ParticularAtm(MethodView):
    particular_atm_service = services.ParticularAtmServices()

    @classmethod
    def get(cls, id):
        return cls.particular_atm_service.get_particular_atm(id)

    @classmethod
    def post(cls):
        return cls.particular_atm_service.post_atm_data()

    @classmethod
    def delete(cls, id):
        return cls.particular_atm_service.delete_particular_atm(id)

    @classmethod
    def put(cls, id):
        return cls.particular_atm_service.put_particular_atm(id)


class AllBranchesData(MethodView):
    branch_service = services.BranchServices()

    @classmethod
    def get(cls):
        return cls.branch_service.get_all_branches_data()


class ParticularBranches(MethodView):
    """
        Particular one branch's GET, PUT & DELETE Methods
    """
    branch_service = services.BranchServices()

    @classmethod
    def get(cls, id):
        return cls.branch_service.get_particular_branch(id)

    @classmethod
    def post(cls):
        return cls.branch_service.post_branch_data()

    @classmethod
    def delete(cls, id):
        return cls.branch_service.delete_particular_branch(id)

    @classmethod
    def put(cls, id):
        return cls.branch_service.put_particular_branch(id)
