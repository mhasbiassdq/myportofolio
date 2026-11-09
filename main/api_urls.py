from django.urls import path
from . import api_views

app_name = 'main_api'

urlpatterns = [
    path('projects/', api_views.project_list, name='api_project_list'),
    path('projects/<uuid:id>/', api_views.project_detail, name='api_project_detail'),
    path('projects/<uuid:id>/star/', api_views.project_star, name='api_project_star'),
]