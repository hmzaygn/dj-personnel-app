from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Personnel(models.Model):
    CHOISES_TITLE = (
        ("TL", "Team Lead"),
        ("MID", "Mid Lead"),
        ("JUN", "Junior"),
    )

    CHOISES_GENDER = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
        ("N", "Prefer Not Say"),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staffed = models.BooleanField(default=False)
    title = models.CharField(choices=CHOISES_TITLE, default="j", max_length=50)
    gender = models.CharField(choices=CHOISES_GENDER, default="n", max_length=50)
    salary = models.PositiveSmallIntegerField()
    start_date = models.DateTimeField()
    department = models.ForeignKey(Department, related_name="personnel", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"