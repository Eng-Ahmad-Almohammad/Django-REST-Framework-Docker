from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    description = models.TextField()
    ISBN = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title


