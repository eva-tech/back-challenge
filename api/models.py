from django.db import models


class Study(models.Model):
    id = models.AutoField(primary_key=True)
    urgency_level = models.TextField(blank=True)
    body_part = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100)
    type = models.TextField()

    class Meta:
        db_table = "studies"


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    birth_date = models.DateField(null=True)
    email = models.EmailField(null=True)
    national_id = models.TextField(null=True)
    study = models.ForeignKey(Study, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "patient"
