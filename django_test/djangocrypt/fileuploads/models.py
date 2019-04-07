from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FileUpload(models.Model):
    description = models.CharField(max_length=100)
    slug = models.SlugField()
    file = models.FileField(default='default.png', upload_to='uploads/')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png',blank=True)
    upload_user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    def snippet(self):
        return self.body[:50] + '...'