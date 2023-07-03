from django.db import models
# Create your models here.

class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ImageField(upload_to="pics")
    title = models.CharField(max_length=100, default="Blog on Programming")
    username = models.CharField(max_length=50, default="Anonymous")
    designation = models.CharField(max_length=150, default="Coder")
    date = models.DateTimeField()
    category = models.CharField(max_length = 500, default="Coding")
    heading_image = models.ImageField(upload_to="Ishan",default="pic.jpg")
    content = models.TextField()

    

    def __str__(self):
        return self.title + ' '+ 'by' + ' ' + self.username 
