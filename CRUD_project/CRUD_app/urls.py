from django.urls import path
from . import views

urlpatterns =[
    path('', views.employee_list, name="employee-list"),
    path('create/', views.create_employee, name="create-employee"),
    path('<int:pk>/update/', views.update_employee, name="update-employee"),
    path('<int:pk>/delete/', views.delete_employee, name="delete-employee"),
]