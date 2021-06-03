from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='generator/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Bmr_result(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    output = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Bmi_result(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=True)
    output = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username