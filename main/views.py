from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm

def show_main(request):
    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "npm": "2506624360",
        "study_program": "Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Fakultas Ilmu Komputer Universitas Indonesia "
            "yang tertarik pada data dan aktif berorganisasi."
        ),
        "experience_list": Experience.objects.all(),
        "project_list": Project.objects.all(),
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

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    
    if title_query:
        projects = projects.filter(title__icontains=title_query)
        
    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def show_projects(request):
    # Mengambil data dari fungsi JSON lalu di-deserialize kembali (sesuai tutorial)
    json_response = get_projects_json(request)
    projects_deserialized = serializers.deserialize("json", json_response.content.decode("utf-8"))
    projects = [project.object for project in projects_deserialized]
    
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "projects.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")
        
    return redirect("main:show_projects")

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