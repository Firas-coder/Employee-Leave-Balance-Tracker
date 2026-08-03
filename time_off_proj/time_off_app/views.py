from django.shortcuts import redirect, render
from .forms import Emp_infoForm
from .models import Emp_info
from .utils import update_emp_info
# Create your views here.
def search_fun(request):
    #Search By Name Code
    search_by_name=request.GET.get('search_by_name_html')
    if search_by_name:
        emp_info=Emp_info.objects.filter(emp_name__icontains=search_by_name)
    else:
        emp_info=Emp_info.objects.all()
    return render(request,'pages/search_p.html',{'emp_info':emp_info})

def add_fun(request):
    # Add New Employee Code
    if request.method=='POST':
        form=Emp_infoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'pages/add_p.html')
    else:
        form=Emp_infoForm()
    return render(request,'pages/add_p.html',{'form':form})

def edit_fun(request,emp_id):
    # Edit Employee And Clculate Balance Automatically By Enter Hour Number Code
    emp_id=Emp_info.objects.get(id=emp_id)
    if request.method=='POST':
        form=Emp_infoForm(request.POST,instance=emp_id)
        if form.is_valid():
            form.save()
            emp_id=Emp_info.objects.get(id=emp_id.id)
            hour_no=emp_id.emp_hour_no
            balance=emp_id.emp_balance
            # Call update_emp_info function to update the employee balance based on the entered hour number
            update_emp_info(emp_id,hour_no,balance)
            return redirect('/')
    return render(request,'pages/edit_p.html',{'form':Emp_infoForm(instance=emp_id)})