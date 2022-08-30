from flask import Blueprint

from BS.Bank.resources import BankDetail, AtmDetail, ParticularAtm, AllBranchesData, ParticularBranches, LoanRequest, \
    InsuranceRequest, TransactMoney, CheckOtp, PayLoanAmount, PayInsuranceAmount, TransferToSaving, SavingToAcc

bank_detail = Blueprint('bank_detail', __name__)

# for bank detail route
bank_detail.add_url_rule('/bank_detail', view_func=BankDetail.as_view('bank_detail'))

# for atm detail route [  CRUD  ]
bank_detail.add_url_rule('/atm_detail', view_func=AtmDetail.as_view('atm_detail'))
bank_detail.add_url_rule('/add_atm', view_func=ParticularAtm.as_view('add_atm'))
bank_detail.add_url_rule('/delete_atm/<int:id>', view_func=ParticularAtm.as_view('delete_atm'))
bank_detail.add_url_rule('/update_atm/<int:id>', view_func=ParticularAtm.as_view('update_atm'))
bank_detail.add_url_rule('/show_atm/<int:id>', view_func=ParticularAtm.as_view('show_particular_atm'))

# for Branches detail route  [  CRUD  ]
bank_detail.add_url_rule('/branches_details', view_func=AllBranchesData.as_view('branches_details'))
bank_detail.add_url_rule('/add_branch', view_func=ParticularBranches.as_view('add_branch'))
bank_detail.add_url_rule('/delete_branch/<int:id>', view_func=ParticularBranches.as_view('delete_branch'))
bank_detail.add_url_rule('/update_branch/<int:id>', view_func=ParticularBranches.as_view('update_branch'))
bank_detail.add_url_rule('/show_branch/<int:id>', view_func=ParticularBranches.as_view('show_particular_branch'))

# for user to apply for loans
bank_detail.add_url_rule('/apply_for_loan', view_func=LoanRequest.as_view('apply_for_loan'))

# for user to apply for insurance
bank_detail.add_url_rule('/apply_for_insurance', view_func=InsuranceRequest.as_view('apply_for_insurance'))

# for user end to transact money to someone's account
bank_detail.add_url_rule('/transfer_to_someone_acc', view_func=TransactMoney.as_view('transfer_to_someone_acc'))
bank_detail.add_url_rule('/otp_check/<int:transaction_id>', view_func=CheckOtp.as_view('otp_check'))

# payback for users
bank_detail.add_url_rule('/pay_loan', view_func=PayLoanAmount.as_view('pay_loan'))
bank_detail.add_url_rule('/pay_insurance', view_func=PayInsuranceAmount.as_view('pay_insurance'))
bank_detail.add_url_rule('/transfer_to_saving', view_func=TransferToSaving.as_view('transfer_to_saving'))
bank_detail.add_url_rule('/transfer_to_account', view_func=SavingToAcc.as_view('transfer_to_account'))
