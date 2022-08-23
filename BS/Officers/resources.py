from flask.views import MethodView
from flask_jwt_extended import jwt_required

from BS.Officers import services
from BS.User.utils import is_loan_officer, is_insurance_officer


# for loan officer starts
class LoanTypeDetails(MethodView):
    """
        LoanType's GET ALL methods
    """
    decorators = [jwt_required(), is_loan_officer()]
    loan_service = services.LoanOfficerservices()

    def get(cls):
        return cls.loan_service.get_all_loan_types()


class ParticularLoanType(MethodView):
    """
        LoanType's GET ALL methods
    """
    decorators = [jwt_required(), is_loan_officer()]
    loan_service = services.LoanOfficerservices()

    @classmethod
    def get(cls, id):
        return cls.loan_service.get_particular_loan_type(id)

    @classmethod
    def post(cls):
        return cls.loan_service.post_particular_loan_type()

    @classmethod
    def put(cls, id):
        return cls.loan_service.put_particular_loan_type(id)

    @classmethod
    def delete(cls, id):
        return cls.loan_service.delete_particular_loan_type(id)


# for loan officer ends

# for insurance officer starts
class InsuranceTypeDetails(MethodView):
    """
        InsuranceType's GET ALL methods
    """
    decorators = [jwt_required(), is_insurance_officer()]
    insurance_service = services.InsuranceServices()

    @classmethod
    def get(cls):
        return cls.insurance_service.get_all_insurance_types()


class ParticularInsuranceType(MethodView):
    """
        InsuranceType's GET/PUT/POST/DELETE for particular one id
    """
    decorators = [jwt_required(), is_insurance_officer()]
    insurance_service = services.InsuranceServices()

    @classmethod
    def get(cls, id):
        return cls.insurance_service.get_particular_insurance_type(id)

    @classmethod
    def post(cls):
        return cls.insurance_service.post_particular_insurance_type()

    @classmethod
    def put(cls, id):
        return cls.insurance_service.put_particular_insurance_type(id)

    @classmethod
    def delete(cls, id):
        return cls.insurance_service.delete_particular_insurance_type(id)

# for insurance officer ends
