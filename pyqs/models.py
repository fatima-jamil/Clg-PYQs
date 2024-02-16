from django.db import models
from django.contrib.auth.models import User

class Firstyear(models.Model):
    sub_name = models.CharField(max_length= 50,null=False)
    sub_code = models.CharField(max_length= 10,null=False)
    session = models.CharField(max_length= 10,null=False)
    sem = models.CharField(max_length= 10,null=False)
    midend = models.CharField(max_length= 10,null=False)
    pdf = models.FileField(null=False)

    def __str__(self):
        return self.sub_code
    

class Core(models.Model):

    sub_name = models.CharField(max_length= 50,null=False)
    sub_code = models.CharField(max_length= 10,null=False)
    dept = models.CharField(max_length= 50,null=False)
    session = models.CharField(max_length= 10,null=False)
    sem = models.CharField(max_length= 10,null=False)
    midend = models.CharField(max_length= 10,null=False)
    pdf = models.FileField(null=False)

    def __str__(self):
        return self.sub_code
    

class ESO(models.Model):

    sub_name = models.CharField(max_length= 50,null=False)
    sub_code = models.CharField(max_length= 10,null=False)
    dept = models.CharField(max_length= 50,null=False)
    session = models.CharField(max_length= 10,null=False)
    sem = models.CharField(max_length= 10,null=False)
    midend = models.CharField(max_length= 10,null=False)
    pdf = models.FileField(null=False)

    def __str__(self):
        return self.sub_code
    

class OE(models.Model):

    sub_name = models.CharField(max_length= 50,null=False)
    sub_code = models.CharField(max_length= 10,null=False)
    dept = models.CharField(max_length= 50,null=False)
    session = models.CharField(max_length= 10,null=False)
    sem = models.CharField(max_length= 10,null=False)
    midend = models.CharField(max_length= 10,null=False)
    pdf = models.FileField(null=False)

    def __str__(self):
        return self.sub_code
    

class Upload(models.Model):

    sub_name = models.CharField(max_length= 50,null=False)
    sub_code = models.CharField(max_length= 10,null=False)
    dept = models.CharField(max_length= 50,null=False)
    sub_type = models.CharField(max_length= 50,null=True)
    session = models.CharField(max_length= 10,null=False)
    sem123= models.CharField(max_length= 10,null=False)
    sem = models.CharField(max_length= 10,null=False)
    midend = models.CharField(max_length= 10,null=False)
    usermail = models.CharField(max_length= 50,null = True)
    pdf = models.FileField(null=False)

    def __str__(self):
        return self.sub_code