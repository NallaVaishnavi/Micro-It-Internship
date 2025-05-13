from django.db import models

class StudentRegister(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    language = models.CharField(max_length=20)
    year = models.IntegerField()
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
