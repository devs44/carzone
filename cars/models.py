from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Car(models.Model):
    state_choice = (
        ('Ktm','Kathmandu'),
        ('Ptn','Patan'),
        ('Lp','Lalitpur'),
        ('Bhkt','Bhaltapur'),
        ('Rmchp','Rammechhap'),
        )
    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now,blank=True)


    def __str__(self):
        return self.car_title
