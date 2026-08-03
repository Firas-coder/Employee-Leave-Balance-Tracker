from django import forms
from .models import Emp_info
class Emp_infoForm(forms.ModelForm):
    class Meta:
        model=Emp_info
        fields='__all__'
        widgets={
            'emp_no':forms.NumberInput(attrs={'placeholder': 'Enter employee number', 'readonly': 'readonly'}),
            'emp_name':forms.TextInput(attrs={'placeholder': 'Enter employee name', 'readonly': 'readonly'}),
            'emp_balance':forms.NumberInput(attrs={'placeholder': 'Enter employee balance', 'readonly': 'readonly'}),
            'emp_date_created':forms.DateInput(attrs={'type':'date', 'placeholder': 'YYYY-MM-DD'}),
            'emp_date_update':forms.DateInput(attrs={'type':'date', 'placeholder': 'YYYY-MM-DD'}),
        }
