from django.urls import path
from main.views import (
    show_main, show_experience, show_projects, 
    create_project, get_projects_json, delete_project,
    create_experience, edit_experience, delete_experience, get_experience_json, 
    register, login_user, logout_user, toggle_star,
    show_education, create_education, delete_education, create_project_ajax,
    create_experience_ajax
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    
    path("projects/", show_projects, name="show_projects"),
    path("projects/add/", create_project, name="create_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"), 
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"), 
    
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star"),
    
    path("education/", show_education, name="show_education"),
    path("education/add/", create_education, name="create_education"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("projects/add-ajax/", create_project_ajax, name="create_project_ajax"),
    path("api/experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
    #path('cetak-admin/', cetak_admin_pws, name='cetak_admin_pws'),
]
