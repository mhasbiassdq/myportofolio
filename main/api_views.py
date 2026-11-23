from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Project
from .serializers import ProjectSerializer
from .permissions import IsPortfolioOwnerOrEditorOrReadOnly


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_logout(request):
    """Menghapus token autentikasi milik pengguna yang sedang login."""
    if request.auth is not None:
        request.auth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def project_list(request):
    """Melihat daftar project atau membuat project baru."""
    if request.method == 'GET':
        q = request.GET.get('q', '')
        projects = Project.objects.all()
        if q:
            projects = projects.filter(title__icontains=q)

        serializer = ProjectSerializer(projects, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def project_detail(request, id):
    """Melihat, mengubah, atau menghapus satu project spesifik."""
    project = get_object_or_404(Project, id=id)

    if request.method == 'GET':
        serializer = ProjectSerializer(project, context={'request': request})
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'
        serializer = ProjectSerializer(
            project,
            data=request.data,
            partial=partial,
            context={'request': request},
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def project_star(request, id):
    """Memberikan atau membatalkan star pada project."""
    project = get_object_or_404(Project, id=id)

    if request.user in project.starred_by.all():
        project.starred_by.remove(request.user)
        is_starred = False
    else:
        project.starred_by.add(request.user)
        is_starred = True

    return Response({
        'is_starred': is_starred,
        'star_count': project.starred_by.count()
    }, status=status.HTTP_200_OK)