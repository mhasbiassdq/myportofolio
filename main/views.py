from django.shortcuts import render
from main.models import Experience

def show_main(request):
    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "npm": "2506624360",
        "study_program": "Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Fakultas Ilmu Komputer Universitas Indonesia "
            "yang tertarik pada data dan aktif berorganisasi."
        ),
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Muhammad Hasbi Assiddiq",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)