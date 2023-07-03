from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50,default="Anonymus")
    lname = models.CharField(max_length=50,default="Anonymus")
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150,default="Technical Error")
    date = models.DateTimeField()
    desc = models.CharField(max_length=100)

    def __str__(self):
        return 'Query By:' + ' ' + self.email