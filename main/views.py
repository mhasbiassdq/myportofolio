import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

from main.models import Experience, Project, Education
from main.forms import ProjectForm, ExperienceForm, EducationForm

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    
    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "npm": "2506624360",
        "study_program": "Sistem Informasi",
        "bio": (
            "Information Systems undergraduate at Universitas Indonesia, specializing in Data Science and Artificial Intelligence. "
            "I am a tech enthusiast and proactive leader passionate about transforming complex data into impactful digital solutions."
        ),
        "last_login": last_login, 
    }
    return render(request, "index.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()
    
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)
        
    experiences_json = serializers.serialize("json", experiences)
    return HttpResponse(experiences_json, content_type="application/json")


def show_experience(request):
    json_response = get_experience_json(request)
    experiences_deserialized = serializers.deserialize("json", json_response.content.decode("utf-8"))
    experiences = [exp.object for exp in experiences_deserialized]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)


@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")
        
    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "form": form,
        "page_title": "Edit Pengalaman",
    }
    return render(request, "experience_form.html", context)


@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
        
    return redirect("main:show_experience")


@login_required(login_url="/login/")
def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")
    
    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "form": form,
        "page_title": "Tambah Pengalaman Baru", 
    }
    return render(request, "experience_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()
    
    if title_query:
        projects = projects.filter(title__icontains=title_query)
        
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "category": project.category,
                "thumbnail": project.thumbnail,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
        
    return JsonResponse(data, safe=False)


def show_projects(request):
    title_query = request.GET.get("title", "").strip()
    
    context = {
        "name": "Muhammad Hasbi Assiddiq", # Ganti pakai namalu
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "projects.html", context)


@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
        
    return redirect("main:show_projects")


@login_required(login_url="/login/")
def create_project(request):
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "form": form,
    }
    return render(request, "projects_form.html", context)


@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)
    return redirect("main:show_projects")

def show_education(request):
    educations = Education.objects.all().order_by('-start_year')
    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "education_list": educations,
    }
    return render(request, "education.html", context)


@login_required(login_url="/login/")
def create_education(request):
    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat Pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "form": form,
    }
    return render(request, "education_form.html", context)


@login_required(login_url="/login/")
def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat Pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Muhammad Hasbi Assiddiq", 
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Muhammad Hasbi Assiddiq", 
        "form": form,
    }
    return render(request, "login.html", context)


def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@require_POST
def create_project_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse(
            {"message": "Anda harus login untuk menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save(commit=False)
        project.save()
        return JsonResponse({
            "message": "Proyek baru berhasil ditambahkan!",
            "pk": str(project.id)
        }, status=201)
    
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

def cetak_admin_pws(request):
    if not User.objects.filter(username='admin_hasbi').exists():
        User.objects.create_superuser('admin_hasbi', 'email@test.com', 'rahasia123')
        return HttpResponse("Sukses, bosht! Akun Superuser 'admin_hasbi' berhasil dicetak di PWS.")
    else:
        return HttpResponse("Akun Superuser 'admin_hasbi' udah ada, langsung login aja.")