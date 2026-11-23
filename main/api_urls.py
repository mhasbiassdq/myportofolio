from django.urls import path
from rest_framework.authtoken import views as authtoken_views

from . import api_views

app_name = 'main_api'

urlpatterns = [
    path('auth/token/', authtoken_views.obtain_auth_token, name='api_token_auth'),
    path('auth/logout/', api_views.api_logout, name='api_token_logout'),
    path('projects/', api_views.project_list, name='api_project_list'),
    path('projects/<uuid:id>/', api_views.project_detail, name='api_project_detail'),
    path('projects/<uuid:id>/star/', api_views.project_star, name='api_project_star'),
]