from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [

    path('', views.home, name='home-page'),
    path('company/', views.company, name='company'),
    path('company/data', views.data_company, name='data-company'),
    path('company/new', views.create_company, name='new-company'),
    path('company/<uuid:pk>', views.edit_company, name='edit-company'),

    # path('test/', views.test, name='test'),

    # path('process-list-full', ProcessList.as_view(), name='process-list-full'),
    # path('process-list-partner', ProcessListPartner.as_view(), name='process-list-partner'),
    # path('process-list-owner', ProcessListOwner.as_view(), name='process-list-owner'),
    # path('process-create', ProcessCreate.as_view(), name='process-create'),
    # path('process-detail/<uuid:pk>', ProcessDetail.as_view(), name='process-detail'),
    # path('process-update/<uuid:pk>', ProcessUpdate.as_view(), name='process-update'),
    # path('process-delete/<uuid:pk>', ProcessDelete.as_view(), name='process-delete'),


]