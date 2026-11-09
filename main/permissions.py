from rest_framework import permissions

class IsPortfolioOwnerOrEditorOrReadOnly(permissions.BasePermission):
    """
    Custom permission sesuai skenario Tugas 6:
    - Pengunjung tanpa login: Read-only (GET, HEAD, OPTIONS).
    - Pengguna biasa: Read-only (Star diizinkan lewat endpoint /star/ khusus).
    - Editor: Read-only + Edit (PUT, PATCH). Dilarang Create (POST) / Delete.
    - Superuser (Pemilik portofolio): Bebas semua akses.
    """
    
    def has_permission(self, request, view):
        # 1. Semua orang (termasuk anonim) boleh melihat data (Read-only)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Tolak request ubah data jika tidak login
        if not request.user or not request.user.is_authenticated:
            return False
            
        # 2. Superuser (Pemilik Portofolio) boleh bebas (POST, PUT, PATCH, DELETE)
        if request.user.is_superuser:
            return True
            
        # 3. Editor hanya boleh mengubah data (PUT, PATCH)
        # (Asumsi user Editor sudah dimasukkan ke dalam grup "Editor" di setup test/admin)
        is_editor = request.user.groups.filter(name="Editor").exists()
        if is_editor and request.method in ['PUT', 'PATCH']:
            return True
            
        # 4. Pengguna biasa ditolak jika mencoba CRUD ke resource utama.
        # (Mereka hanya boleh nge-star yang nanti diatur via IsAuthenticated di view star-nya)
        return False

    def has_object_permission(self, request, view, obj):
        # Logika object-level sama persis dengan aturan has_permission di atas
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
            
        is_editor = request.user.groups.filter(name="Editor").exists()
        if is_editor and request.method in ['PUT', 'PATCH']:
            return True
            
        return False