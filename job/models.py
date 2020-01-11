from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    desc = models.CharField(max_length=100,null= True)
    url = models.CharField(max_length=200,null= True)

    def __str__(self):
       return self.summary
