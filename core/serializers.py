from rest_framework import serializers
from .models import *




class HomepageSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField()
    class Meta:
        model = Homepage
        fields = '__all__'



class ServerSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField()
    class Meta:
        model = Servers
        fields = '__all__'

