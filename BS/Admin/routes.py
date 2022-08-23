from flask import Blueprint

from BS.Admin.resources import UserRolesData, UserData, GetAllBranchOfficers, GetAllLoanOfficers, \
    GetAllInsuranceOfficers, AccountTypeData, CardRequests

admin = Blueprint('admin', __name__)

# GET/POST FOR USER ROLE
admin.add_url_rule('/user_roles', view_func=UserRolesData.as_view('user_roles'))
# DELETE FOR USER ROLE
admin.add_url_rule('/delete_user_role/<int:id>', view_func=UserRolesData.as_view('delete_user_role'))
# POST FOR USER ENTRY
admin.add_url_rule('/new_user', view_func=UserData.as_view('new_user'))
admin.add_url_rule('/all_users', view_func=UserData.as_view('all_users'))

# GET ALL BANK BRANCH OFFICERS
admin.add_url_rule('/all_branch_officers', view_func=GetAllBranchOfficers.as_view('all_branch_officers'))
admin.add_url_rule('/delete_branch_officer/<int:id>', view_func=GetAllBranchOfficers.as_view('delete_branch_officer'))

# GET ALL BANK LOAN OFFICERS
admin.add_url_rule('/all_loan_officers', view_func=GetAllLoanOfficers.as_view('all_loan_officers'))
admin.add_url_rule('/delete_loan_officer/<int:id>', view_func=GetAllLoanOfficers.as_view('delete_loan_officer'))

# GET ALL BANK INSURANCE OFFICERS
admin.add_url_rule('/all_insurance_officers', view_func=GetAllInsuranceOfficers.as_view('all_insurance_officers'))
admin.add_url_rule('/delete_insurance_officer/<int:id>',
                   view_func=GetAllInsuranceOfficers.as_view('delete_insurance_officer'))

# FOR ACCOUNT TYPE BY USER [ GET ALL/POST NEW/DELETE EXISTED ]
admin.add_url_rule('/all_account_types', view_func=AccountTypeData.as_view('all_acc_types'))
admin.add_url_rule('/all_account_types/<int:id>', view_func=AccountTypeData.as_view('delete_acc_type'))

# Card-requests by users
admin.add_url_rule('/all_card_requests', view_func=CardRequests.as_view('all_cards_requests'))
admin.add_url_rule('/approval_for_card/<int:id>', view_func=CardRequests.as_view('approval_for_card'))