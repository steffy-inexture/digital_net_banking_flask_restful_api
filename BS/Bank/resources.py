from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity

from BS.Bank import services
from BS.User.utils import is_user


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


class LoanRequest(MethodView):
    decorators = [jwt_required(), is_user()]
    loan_request_service = services.LoanRequestService()

    @classmethod
    def post(cls):
        return cls.loan_request_service.loan_request()

class InsuranceRequest(MethodView):
    decorators = [jwt_required(), is_user()]
    insurance_request_service = services.InsuranceRequestService()

    @classmethod
    def post(cls):
        return cls.insurance_request_service.insurance_request()

class TransactMoney(MethodView):
    decorators = [jwt_required(), is_user()]
    transact_money_service = services.TransactMoneyService()

    @classmethod
    def post(cls):
        return cls.transact_money_service.account_transfer()

class CheckOtp(MethodView):
    decorators = [jwt_required(), is_user()]
    transact_money_service = services.TransactMoneyService()

    @classmethod
    def post(cls,transaction_id):
        return cls.transact_money_service.check_otp(transaction_id)

class PayLoanAmount(MethodView):
    decorators = [jwt_required(), is_user()]
    service = services.PayBackService()

    @classmethod
    def post(cls):
        return cls.service.pay_loan()

class PayInsuranceAmount(MethodView):
    decorators = [jwt_required(), is_user()]
    service = services.PayBackService()

    @classmethod
    def post(cls):
        return cls.service.pay_insurance()


class TransferToSaving(MethodView):
    decorators = [jwt_required(), is_user()]
    service = services.PayBackService()

    @classmethod
    def post(cls):
        return cls.service.transfer_to_saving()

class SavingToAcc(MethodView):
    decorators = [jwt_required(), is_user()]
    service = services.PayBackService()

    @classmethod
    def post(cls):
        return cls.service.transfer_to_account()