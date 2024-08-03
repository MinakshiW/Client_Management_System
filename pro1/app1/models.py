from django.db import models

# Create your models here.
class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    company = models.CharField(max_length=50, null=False)
    email = models.EmailField(unique=True)
    dept = models.CharField(max_length=50, null=False)
    doj = models.DateField()
    status = models.CharField(max_length=34)
    domain = models.CharField(max_length=34)