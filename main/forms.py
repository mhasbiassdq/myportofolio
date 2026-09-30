from django.forms import ModelForm, TextInput, Textarea, Select, URLInput
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from main.models import Project, Experience, Education
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "category", "thumbnail"]
        
        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "category": "Kategori Proyek",
            "thumbnail": "URL Thumbnail Gambar",
        }
        
        widgets = {
            "title": TextInput(attrs={
                "placeholder": "Contoh: Lomba UI/UX Design", 
                "maxlength": 255
            }),
            "description": Textarea(attrs={
                "placeholder": "Ceritakan proyekmu secara singkat...", 
                "rows": 3
            }),
            "category": Select(), 
            "thumbnail": URLInput(attrs={
                "placeholder": "https://url-gambar-kamu.com"
            }),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data['title']).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data['description']).strip()
        
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category", "thumbnail"]
        
        labels = {
            "title": "Posisi / Peran",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Logo / Gambar",
        }
        
        widgets = {
            "title": TextInput(attrs={
                "placeholder": "Contoh: Ketua BEM / Data Science Intern", 
                "maxlength": 255
            }),
            "description": Textarea(attrs={
                "placeholder": "Ceritakan pengalaman dan tanggung jawabmu...", 
                "rows": 3
            }),
            "category": Select(),
            "thumbnail": URLInput(attrs={
                "placeholder": "https://url-gambar-kamu.com"
            }),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data['title']).strip()
        if not title:
            raise ValidationError("Posisi atau peran tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data['description']).strip()

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'start_year', 'end_year', 'description']