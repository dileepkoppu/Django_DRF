from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import contact

User=get_user_model()


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number','name','email','password']



class contactSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = contact
        fields =['id','phone_number','name','spam']
        read_only_fields=['id','phone_number','name']