from flask import Blueprint

from BS.Bank.resources import BankDetail, AtmDetail, ParticularAtm, AllBranchesData, ParticularBranches

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
