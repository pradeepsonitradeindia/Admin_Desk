from django.db import models

class Person(models.Model):
    username = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username