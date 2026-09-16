from django.shortcuts import render, redirect
from django.contrib import messages
from main.models import Experience, Project
from main.forms import ProjectForm

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

def show_experience(request):
    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_projects(request):
    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "project_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)

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