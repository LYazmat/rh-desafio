from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Home page
    path('', views.home, name='home-page'),

    # CRUD Company
    path('company/', views.company, name='company'),
    path('company/data', views.data_company, name='data-company'),
    path('company/new', views.create_company, name='new-company'),
    path('company/<uuid:pk>', views.edit_company, name='edit-company'),
    path('company/delete/<uuid:pk>', views.delete_company, name='delete-company'),
    path('company/logo/<uuid:pk>', views.logo_company, name='logo-company'),

    # CRUD Department
    path('company/department/', views.department, name='department'),
    path('company/department/data', views.data_department, name='data-department'),
    path('company/department/new', views.create_department, name='new-department'),
    path('company/department/<uuid:pk>', views.edit_department, name='edit-department'),
    path('company/delete/department/<uuid:pk>', views.delete_department, name='delete-department'),
    path('company/department/logo/<uuid:pk>', views.logo_department, name='logo-department'),

    # CRUD Employee
    path('company/department/employee/', views.employee, name='employee'),
    path('company/department/employee/data', views.data_employee, name='data-employee'),
    path('company/department/employee/new', views.create_employee, name='new-employee'),
    path('company/department/employee/<uuid:pk>', views.edit_employee, name='edit-employee'),
    path('company/delete/department/employee/<uuid:pk>', views.delete_employee, name='delete-employee'),


    path('test/', views.test, name='test'),

    # path('process-list-full', ProcessList.as_view(), name='process-list-full'),
    # path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
    # path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
    # path('process-create', ProcessCreate.as_view(), name='process-create'),
    # path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
    # path('process-update/<uuid:pk>', ProcessUpdate.as_view(), name='process-update'),
    # path('process-delete/<uuid:pk>', ProcessDelete.as_view(), name='process-delete'),


]