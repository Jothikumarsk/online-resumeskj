from django.db import models


# Create your models here.
class Summary(models.Model):
   name = models.CharField(max_length=50)
   title = models.CharField(max_length=100)
   address = models.CharField(max_length=1000, blank=True)
   emailid = models.CharField(max_length=50, blank=True)
   summary = models.CharField(max_length=2083)
   
   
class SocialMedia(models.Model):
    id = models.CharField(primary_key=True, max_length = 50, auto_created=True)
    social = models.CharField(max_length=50)
    Phone = models.CharField(max_length=200, blank=True)
    image_url = models.CharField(max_length=2083)


class WorkExperience(models.Model):
    companyname = models.CharField(max_length=300)
    title = models.CharField(max_length=100, blank=True)
    year = models.CharField(max_length=100,blank=True)
    responsibilities = models.CharField(max_length=2083)


class Education(models.Model):
    university = models.CharField(max_length=500)
    course = models.CharField(max_length=1000)
    year = models.DateField()
    content = models.CharField(max_length=500,blank=True)
    gpa = models.CharField(max_length=100,blank=True)


class Skills(models.Model):
    organisation = models.CharField(max_length=350)
    url = models.CharField(max_length=2083, blank=True)
    year = models.DateField()


class Awards(models.Model):
    certificate = models.CharField(max_length = 500)
    url = models.CharField(max_length=2083)

