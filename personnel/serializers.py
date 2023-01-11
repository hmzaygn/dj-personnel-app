from rest_framework import serializers
from django.utils.timezone import now

from .models import Department, Personnel


class PersonnelSerializer(serializers.ModelSerializer):

    days_since_joined = serializers.SerializerMethodField()
    department = serializers.StringRelatedField(read_only=True)
    department_id = serializers.IntegerField()
    
    class Meta:
        model = Personnel
        fields = (
            "id",
            "days_since_joined",
            # "create_user",
            "first_name",
            "last_name",
            "last_name",
            "is_staffed",
            "title",
            "gender",
            "salary",
            "start_date",
            "department",
            "department_id"
        )

    def get_days_since_joined(self, obj):
        return (now() - obj.start_date).days

class DepartmentSerializer(serializers.ModelSerializer):

    personnel = PersonnelSerializer(many=True, read_only=True)
    personnel_count = serializers.SerializerMethodField()

    
    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "personnel_count",
            "personnel",
        )
    
    def get_personnel_count(self, obj):
        return obj.personnel.count()