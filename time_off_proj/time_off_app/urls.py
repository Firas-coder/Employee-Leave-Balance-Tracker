from django.urls import path
from . import views
urlpatterns = [
    path('',views.search_fun,name='search'),
    path('add/',views.add_fun,name='add'),
    path('edit/<int:emp_id>',views.edit_fun,name='edit'),
    ]
