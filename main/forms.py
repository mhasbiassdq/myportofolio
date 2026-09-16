from django.forms import ModelForm, TextInput, Textarea, Select, URLInput
from main.models import Project

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
            "category": Select(), # Otomatis mengambil pilihan dari PROJECT_CHOICES
            "thumbnail": URLInput(attrs={
                "placeholder": "https://url-gambar-kamu.com"
            }),
        }