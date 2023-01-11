from django.shortcuts import render
from rest_framework import viewsets

from .models import Department, Personnel
from .serializers import DepartmentSerializer, PersonnelSerializer
from .permissions import IsStaffOrReadOnly


class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsStaffOrReadOnly,)

class PersonnelView(viewsets.ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = (IsStaffOrReadOnly,)

