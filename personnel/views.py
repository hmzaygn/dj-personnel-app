from django.shortcuts import render
from rest_framework import viewsets

from .models import Department, Personnel
from .serializers import DepartmentSerializer, PersonnelSerializer


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PersonnelView(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

