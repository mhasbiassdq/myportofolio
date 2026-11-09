from rest_framework import serializers
from django.utils.html import strip_tags
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer untuk model Project.
    Mengubah data model menjadi JSON dan melakukan validasi input.
    """
    # Field read-only tambahan hasil perhitungan untuk fitur Star
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()

    class Meta:
        model = Project
        # Mendefinisikan fields secara eksplisit (Dilarang pakai '__all__' di Tugas 6)
        fields = [
            'id', 
            'title', 
            'description', 
            'category', 
            'thumbnail', 
            'started_at', 
            'ended_at', 
            'star_count', 
            'is_starred'
        ]
        # Mencegah field ini diubah oleh request POST/PUT/PATCH client
        read_only_fields = ['id', 'started_at']

    def get_star_count(self, obj):
        """Menghitung total pengguna yang memberikan star pada project ini."""
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        """Mengecek apakah user yang sedang login sudah memberikan star."""
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.starred_by.filter(id=request.user.id).exists()
        return False

    def validate_title(self, value):
        """Membersihkan input teks 'title' untuk mencegah XSS."""
        return strip_tags(value)

    def validate_description(self, value):
        """Membersihkan input teks 'description' untuk mencegah XSS."""
        return strip_tags(value)