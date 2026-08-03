from django.db import models

# Create your models here.
class Emp_info(models.Model):
    emp_no=models.IntegerField(null=True)#employee number
    emp_name=models.CharField(max_length=100,null=True)#employee name
    emp_balance=models.IntegerField(null=True)#employee balance
    emp_hour_no=models.IntegerField(null=True)#employee hour number 
    emp_date_created=models.DateField(null=True)#employee date
    emp_date_update=models.DateField(auto_now=True)#employee date update
    def __str__(self):
        return self.emp_name
