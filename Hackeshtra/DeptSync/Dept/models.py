from django.db import models

# Create your models here.

#model for onging projects
class onGoingProjects(models.Model):
    DeptName =  models.CharField(max_length = 100 , default="Untitled Project")
    District =  models.CharField(max_length = 100, default="Untitled Project")
    prjName = models.CharField(max_length = 100)
    prjDescription = models.CharField(max_length = 200)
    prjAgency =  models.CharField(max_length = 100)
    prjAgencyLicense = models.FileField(upload_to='uploads/Agency')
    prjFinance = models.FileField(upload_to='uploads/Finance')

#model for Resource request
class resourceRequest(models.Model):
    DeptName = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    resource = models.CharField(max_length = 100)
    replyDept = models.CharField(max_length = 100 , default="Untitled Project")
    replyDist = models.CharField(max_length = 100 , default="Untitled Project")
    replyDescription = models.CharField(max_length = 300 , default="Untitled Project")

class LoginPage(models.Model):
    userId =  models.CharField(max_length = 100 , default="Untitled Project")
    password =  models.CharField(max_length = 100, default="Untitled Project")

class makeObjection(models.Model):
    DeptName = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    objection = models.CharField(max_length=100)