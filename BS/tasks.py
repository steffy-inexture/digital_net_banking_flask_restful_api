from BS import celery
from BS.Bank.models import Loans, Insurances
from BS.Bank.utils import send_mail_for_pending_loan
from BS.User.models import User


@celery.task()
def loan_detail():
    loans = Loans.query.all()
    for loan in loans:
        send_mail_for_pending_loan(loan.id)

@celery.task()
def insurance_detail():
    insurances = Insurances.query.all()
    print("this is insurances",insurances)