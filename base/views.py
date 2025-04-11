from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Project, Profile
from .serializers import ProjectSerializer, ProfileSerializer
from django.contrib.auth.models import AnonymousUser


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/projects/',
        'api/projects/create/',

        'api/projects/upload/',

        'api/projects/<id>/reviews/',

        'api/projects/top/',
        'api/projects/<id>/',

        'api/projects/delete/<id>/',
        'api/projects/<update>/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getUserProfile(request):
    profile = Profile.objects.first()
    if profile:
        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)
    else:
        return Response({'message': 'User profile not found'}, status=404)

@api_view(['GET'])
def getProjects(request):
    try:
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
    except Project.DoesNotExist:
        return Response({'message': 'No projects available'})
    return Response(serializer.data)

@api_view(['GET'])
def getProject(request, pk):
    project = Project.objects.get(_id=pk)
    serializer = ProjectSerializer(project, many=False)
    return Response(serializer.data)