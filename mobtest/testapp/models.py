from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contractor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    nationality = models.CharField(max_length=500)
    comment = models.CharField(max_length=500)
    pay_rate = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username
    


class ContractorApplication(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=500)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
