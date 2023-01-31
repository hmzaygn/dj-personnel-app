from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Department, Personnel
from .serializers import (
    DepartmentSerializer,
    PersonnelSerializer,
    DepartmentPersonnelSerializer,
)
from .permissions import (
    IsStaffOrReadOnly,
    IsOwnerAndStaffOrReadOnly,
    )

class DepartmentView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]


class PersonnelListCreateView(generics.ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.request.user.is_staff:
            personnel = self.perform_create(serializer)
            data = {
                "message": f"Personnel {personnel.first_name} saved successfully",
                "personnel": serializer.data
            }
        else:
            data = {
                "message": "You aren't authorized to perform this operation!!"
            }
            headers = self.get_success_headers(data)
            return Response(data, status=status.HTTP_401_UNAUTHORIZED, headers=headers)

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)
    
    def perform_create(self, serializer):
        person = serializer.save()
        return person


class PersonnelGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAuthenticated, IsOwnerAndStaffOrReadOnly]

    def delete(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return self.destroy(request, *args, **kwargs)
        else:
            data = {
                "message": "You aren't authorized to perform this operation!!"
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)


class DepartmentPersonnelView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentPersonnelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        name = self.kwargs["department"]  # catches keywords from endpoint dynamically
        return Department.objects.filter(name__iexact=name)  # not case sensitive



