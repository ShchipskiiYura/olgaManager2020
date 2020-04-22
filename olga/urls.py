from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

employee_list = EmployeeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

employee_detail = EmployeeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

office_list = OfficeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

office_detail = OfficeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

project_list = ProjectViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

project_detail = ProjectViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

team_list = TeamViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

team_detail = TeamViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

company_list = CompanyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

company_detail = CompanyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

sprint_list = SprintViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

sprint_detail = SprintViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('query-employee/', EmployeeQueryset.as_view()),
    path('query-company/', CompanyQueryset.as_view()),
    path('query-office/', OfficeQueryset.as_view()),
    path('query-team/', TeamQueryset.as_view()),
    path('query-project/', ProjectQueryset.as_view()),
    path('query-programer/', ProgQueryset.as_view()),
    path('query-task/', TaskQueryset.as_view()),
    path('query-sprint', SprintQueryset.as_view()),
    path('employee/', employee_list, name='employee_list'),
    path('employee/<int:pk>', employee_detail, name='employee_detail'),
    path('office/', office_list, name='office_list'),
    path('office/<int:pk>', office_detail, name='office_detail'),
    path('project/', project_list, name='project_list'),
    path('project/<int:pk>', project_detail, name='project_detail'),
    path('team/', team_list, name='team_list'),
    path('team/<int:pk>', team_detail, name='team_detail'),
    path('company/', company_list, name='company_list'),
    path('company/<int:pk>', company_detail, name='company_detail'),
    path('sprint/', sprint_list, name='sprint_list'),
    path('sprint/<int:pk>', sprint_detail, name='sprint_detail'),

]