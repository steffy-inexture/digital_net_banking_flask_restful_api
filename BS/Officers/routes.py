from flask import Blueprint

from BS.Officers.resources import LoanTypeDetails, ParticularLoanType, InsuranceTypeDetails, ParticularInsuranceType, \
    LoanRequests, InsuranceRequests

officers = Blueprint('officers', __name__)

# for all loan type route [ only access to Loan officers ]
officers.add_url_rule('/show_all_loan_types', view_func=LoanTypeDetails.as_view('show_all_loan_types'))
officers.add_url_rule('/show_loan_type/<int:id>', view_func=ParticularLoanType.as_view('show_loan_type'))
officers.add_url_rule('/add_loan_type', view_func=ParticularLoanType.as_view('add_loan_type'))
officers.add_url_rule('/update_loan_type/<int:id>', view_func=ParticularLoanType.as_view('update_loan_type'))
officers.add_url_rule('/delete_loan_type/<int:id>', view_func=ParticularLoanType.as_view('delete_loan_type'))

# for all insurance type route [ only access to insurance officers ]
officers.add_url_rule('/show_all_insurance_types', view_func=InsuranceTypeDetails.as_view('show_all_insurance_types'))
officers.add_url_rule('/show_insurance_type/<int:id>', view_func=ParticularInsuranceType.as_view('show_insurance_type'))
officers.add_url_rule('/add_insurance_type', view_func=ParticularInsuranceType.as_view('add_insurance_type'))
officers.add_url_rule('/update_insurance_type/<int:id>',
                      view_func=ParticularInsuranceType.as_view('update_insurance_type'))
officers.add_url_rule('/delete_insurance_type/<int:id>',
                      view_func=ParticularInsuranceType.as_view('delete_insurance_type'))

# all loan requests
officers.add_url_rule('/show_all_loan_requests', view_func=LoanRequests.as_view('show_all_loan_requests'))
officers.add_url_rule('/update_loan_status/<int:id>', view_func=LoanRequests.as_view('update_loan_status'))

# all insurance requests
officers.add_url_rule('/show_all_insurance_requests',
                      view_func=InsuranceRequests.as_view('show_all_insurance_requests'))
officers.add_url_rule('/update_insurance_status/<int:id>',
                      view_func=InsuranceRequests.as_view('update_insurance_status'))
