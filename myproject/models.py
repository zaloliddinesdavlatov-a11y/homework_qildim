from django.db import models

class yangiliklar(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    image = models.ImageField(upload_to='image/')
    author = models.CharField(max_length=120)

    def __str__(self):
        return self.title
    
