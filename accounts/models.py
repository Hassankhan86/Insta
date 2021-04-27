
# Create your models here.
from django.db import models


# Create your models here.
class Account(models.Model):
    userid = models.TextField(max_length=50, default=None, blank=True)
    password = models.TextField(max_length=50, default=None, blank=True)
    status = models.IntegerField( default=1, blank=True)

    def __str__(self):
        return self.userid



class Profile(models.Model):
    # account = models.ForeignKey(Account,on_delete=models.CASCADE, default=None,null=True)
    follow = models.BooleanField(default=0)
    comment =models.BooleanField(default=0)
    like = models.BooleanField(default=0)
    story = models.BooleanField(default=0)

class Comments(models.Model):
    title = models.TextField(max_length=100, default=None, blank=True)
