from django.db import models

# Create models here to tell how our data looks like. to imic DB.

class User(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self): # to create a string version of this model; to handle like print(user)
        return self.name
