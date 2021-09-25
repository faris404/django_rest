from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

   class Meta:
      model = User
      fields = ['id','first_name','last_name', 'email', 'password']
      extra_kwargs = {"id": {"required": False, "allow_null": True}}



   def create(self, validated_data):
      password = validated_data.pop('password')
      user = User(
         **validated_data
      )
      user.set_password(password)
      user.save()
      user.groups.add(2)
      
      return user

# class UserSerializer(serializers.Serializer):
#    email = serializers.EmailField()
#    first_name = serializers.CharField(max_length=50)
#    last_name = serializers.CharField(max_length=50)
#    password = serializers.CharField(max_length=50)
