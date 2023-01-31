from rest_framework import serializers
from django.utils.timezone import now
from .models import Department, Personnel

class DepartmentSerializer(serializers.ModelSerializer):

    personnel_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "personnel_count",
        )
    
    def get_personnel_count(self, obj):
        return obj.personnels.count()


class PersonnelSerializer(serializers.ModelSerializer):

    create_user_id = serializers.IntegerField(required=False)
    create_user = serializers.StringRelatedField()
    days_since_joined = serializers.SerializerMethodField()
    department = serializers.StringRelatedField()
    department_id = serializers.IntegerField()

    class Meta:
        model = Personnel
        fields = (
            "id",
            "department",
            "department_id",
            "create_user",
            "create_user_id",
            "first_name",
            "last_name",
            "title",
            "gender",
            "salary",
            "start_date",
            "days_since_joined",
        )

    def create(self, validated_data):
        validated_data["create_user_id"] = self.context["request"].user.id
        instance = Personnel.objects.create(**validated_data)
        return instance

    def get_days_since_joined(self, obj):
        return (now() - obj.start_date).days


class DepartmentPersonnelSerializer(serializers.ModelSerializer):

    personnel_count = serializers.SerializerMethodField()
    personnels = PersonnelSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = (
            "id",
            "name",
            "personnel_count",
            "personnels",
        )

    def get_personnel_count(self, obj):
        return obj.personnels.count()


