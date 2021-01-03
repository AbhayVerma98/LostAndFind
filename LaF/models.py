from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.




class Lost(models.Model):
    CHOICE = (
        ('Select Age', 'Select Age'), ('0-5', '0-5'), ('6-10', '6-10'), ('11-15', '11-15'), ('16-20', '16-20'),
        ('21-25', '21-25'), ('26-30', '26-30'), ('31-35', '31-35'),('36-40','36-40'), ('41-45', '46-50'), ('51-55', '51-55'),
        ('56-60', '56-60'),
        ('61-65', '61-65'), ('66-70', '66-70'), ('71-75', '71-75'), ('76-80', '76-80'), ('81-85', '81-85'),
        ('86-90', '86-90'),
    )
    name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50,blank=True,null=True)
    mother_name=models.CharField(max_length=50,blank=True,null=True)
    age=models.CharField(max_length=15,choices=CHOICE)
    image=models.ImageField(blank=True,null=True)
    mobile_no=models.IntegerField(null=True)
    state=models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city_or_village = models.CharField(max_length=100)
    PIN_code = models.IntegerField(null=True)
    aadhaar_no=models.IntegerField(blank=True,null=True)
    description=models.TextField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.name

class Find(models.Model):
    CHOICE = (
        ('Select Age', 'Select Age'), ('0-5', '0-5'), ('6-10', '6-10'), ('10-15', '10-15'), ('16-20', '16-20'),
        ('21-25', '21-25'), ('26-30', '26-30'), ('31-35', '31-35'),('36-40','36-40'), ('41-45','41-45'), ('46-50','46-50'), ('51-55', '51-55'),
        ('56-60', '56-60'),
        ('61-65', '61-65'), ('66-70', '66-70'), ('71-75', '71-75'), ('76-80', '76-80'), ('81-85', '81-85'),
        ('86-90', '86-90'),
    )
    name=models.CharField(max_length=50,null=True)
    father_name=models.CharField(max_length=50,blank=True,null=True)
    mother_name=models.CharField(max_length=50,blank=True,null=True)
    age = models.CharField(choices=CHOICE, max_length=15, blank=True, null=True)
    image=models.ImageField(blank=True,null=True)
    mobile_no=models.IntegerField(null=True,blank=True)
    state=models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city_or_village = models.CharField(max_length=100)
    PIN_code = models.IntegerField(null=True,blank=True)
    aadhaar_no = models.IntegerField(null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name+' '+self.state












