from rest_framework import serializers
from django.contrib.auth.models import User
from todoApp.models import TodoModel


class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["username","email","password"]
        
        
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    
    
class TodoSerilizer(serializers.ModelSerializer):
    owner=UserSerializer(read_only=True)
    class Meta:
        model=TodoModel
        fields="__all__"
        read_only_fields=["id","owner","crearted_date"]