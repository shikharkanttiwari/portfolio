from django.db import models

class Service(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)

    def __str__(self):
       return self.title

#create a migration
#migrate
#add to admin
