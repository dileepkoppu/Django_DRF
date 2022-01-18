from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db.models.signals import post_save


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\d{3}[-\s]?\d{3}[-\s]?\d{4}$', message="Phone number is invaild.")

    phone_number= models.CharField(validators=[phone_regex],unique=True,max_length=10)

    name = models.CharField(max_length=50)

    spam = models.BooleanField(default=False)

    username = None

    USERNAME_FIELD = 'phone_number'
    
    def __str__(self):
        return self.phone_number
    

class contact(models.Model):
    under_user=models.ForeignKey(User, verbose_name="under_user", blank=True, null=True,
        on_delete=models.SET_NULL)

    name=models.CharField(max_length=10,default='Anonymous')

    phone_regex = RegexValidator(regex=r'^([+]?\d{1,2}[-\s]?|)\d{3}[-\s]?\d{3}[-\s]?\d{4}$', message="Phone number is invaild.")

    phone_number= models.CharField(validators=[phone_regex], max_length=17)

    email=models.EmailField( max_length=254,null=True,blank=True)

    spam = models.BooleanField(default=False)

    registered = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        contact.objects.create(name=instance.name,phone_number=instance.phone_number,registered=True)
    
post_save.connect(post_user_created_signal, sender=User)