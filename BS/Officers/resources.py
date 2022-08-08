from flask.views import MethodView

from BS.Officers import services


# for loan officer starts
class LoanTypeDetails(MethodView):
    """
        LoanType's GET ALL methods
    """

    def get(self):
        return services.get_all_loan_types()


class ParticularLoanType(MethodView):
    """
        LoanType's GET ALL methods
    """

    def get(self, id):
        return services.get_particular_loan_type(id)

    def post(self):
        return services.post_particular_loan_type()

    def put(self, id):
        return services.put_particular_loan_type(id)

    def delete(self, id):
        return services.delete_particular_loan_type(id)


# for loan officer ends

# for insurance officer starts
class InsuranceTypeDetails(MethodView):
    """
        InsuranceType's GET ALL methods
    """

    def get(self):
        return services.get_all_insurance_types()


class ParticularInsuranceType(MethodView):
    """
        InsuranceType's GET/PUT/POST/DELETE for particular one id
    """

    def get(self, id):
        return services.get_particular_insurance_type(id)

    def post(self):
        return services.post_particular_insurance_type()

    def put(self, id):
        return services.put_particular_insurance_type(id)

    def delete(self, id):
        return services.delete_particular_insurance_type(id)

# for insurance officer ends
