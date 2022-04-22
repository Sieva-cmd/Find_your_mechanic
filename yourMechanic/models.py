from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer',default=False)
    is_mechanic = models.BooleanField('Is mechanic', default=False)

User = get_user_model()
phone_number_validator = RegexValidator(
    regex=r'^[0-9 \(\)]{10,12}$', message="Phone numbers must begin with +2547.... or 07..."
)

class Customer(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='name')
    description = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True, validators=[phone_number_validator])
    email = models.EmailField()
    location = models.CharField(max_length=100, null=True, blank=True)
    image = CloudinaryField('image', blank=True)
    def __str__(self):
        return str(self.username.username)


class Mechanic(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='customer_name')
    speciality = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True, validators=[phone_number_validator])
    location = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.name.name)


class Engine(models.Model):
    part = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    image = CloudinaryField('photo', blank=True)
    payment = models.DecimalField(decimal_places=2, max_digits=40, default=2000)
    def __str__(self):
        return str(self.part)

        

class FullBodyPaint(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='user') 
    part = models.TextField()
    description = models.TextField(null=True,blank=True)
    mechanic = models.OneToOneField(User,on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=20)

class StereoSetup(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='stereo') 
    part = models.TextField()
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)

class EngineRepair(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,related_name='enginerepair') 
    part = models.TextField()
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)

class Customer(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

class Mechanic(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

