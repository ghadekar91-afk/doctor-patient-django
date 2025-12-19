from django.db import models

class Patient_Info(models.Model):
    id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    disease = models.CharField(max_length=100)
    admitted_date = models.DateField()

    def __str__(self):
        return self.patient_name
