from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='projects/')
    repository = models.URLField()
    skills = models.ManyToManyField(Skill)
    
    def __str__(self):
        return f'{self.title} | {self.year}'
    