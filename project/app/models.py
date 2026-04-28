# app/models.py

from django.db import models

class Insurance(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    policy_type = models.CharField(max_length=100)
    nominee = models.CharField(max_length=100)
    coverage_amount = models.CharField(max_length=50)

    def __str__(self):
        return self.name
