from django.db import models


class Doctor_Info(models.Model):
    id = models.AutoField(primary_key=True)
    Registration_number = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    Qulification = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    Experiance = models.IntegerField()
    timing = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    Hospital_address = models.TextField()

    def __str__(self):
        return self.name
