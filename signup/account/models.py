from django.db import models

# Create your models here.
class NewData(models.Model):
    title=models.CharField(max_length=200)
    name=models.CharField(max_length=200,default='anonymous')
    content=models.TextField()
    last_modified=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class valid(models.Model):
    male='M'
    female='F'
    Gender_choice=(
        (male,'male'),
        (female,'female'),
    )   

    username=models.CharField(max_length=20,blank=False,null=False)
    text=models.TextField(blank=False,null=False)
    gender=models.CharField(max_length=6,choices=Gender_choice,default=male)
    time=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username
    