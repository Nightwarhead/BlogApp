from django.db import models
<<<<<<< HEAD
from django.urls import reverse
=======
from django.urls import reverse         #forms

>>>>>>> 61efa8e2388f5025baa874c4cafb268c0ed50665
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    body = models.TextField()
    def __str__(self):
        return self.title
<<<<<<< HEAD
    
=======
>>>>>>> 61efa8e2388f5025baa874c4cafb268c0ed50665
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])
