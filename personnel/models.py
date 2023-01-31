from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

TITLE = (
    ("Team Lead", "LEAD"),
    ("Mid Lead", "MID"),
    ("Junior", "JUN"),
)

GENDER = (
    ("Female", "F"),
    ("Male", "M"),
    ("Other", "O"),
    ("Prefer Not Say", "N"),
)

class Personnel(models.Model):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="personnels")
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=15, choices=TITLE)
    gender = models.CharField(max_length=15, choices=GENDER)
    salary = models.IntegerField(default=2500)
    start_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} : {self.first_name}"

