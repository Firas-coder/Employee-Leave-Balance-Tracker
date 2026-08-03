from .models import Emp_info
from django.shortcuts import redirect
def update_emp_info(emp_id, hour_no, balance):
    # This function updates the employee balance based on the entered hour number.
    try:
        if hour_no == 6:
            balance -= 1
            hour_no = 0
            emp_id.emp_balance = balance
            emp_id.emp_hour_no = hour_no
            emp_id.save()
        else:
            print("Hour number is not 6. No update performed.")
    except Emp_info.DoesNotExist:
        print("Employee with the given ID does not exist.")
