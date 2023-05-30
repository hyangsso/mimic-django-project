from django.db import models

# Create your models here.
class patientInformation(models.Model):
    subjectid = models.IntegerField(max_length=4)
    age = models.IntegerField(max_length=3)
    sex = models.BooleanField()
    height = models.FloatField(max_length=3)
    weight = models.FloatField(max_length=3)
    bmi = models.FloatField(max_length=2)
    
    def __str__(self):
        return self.sex
    
