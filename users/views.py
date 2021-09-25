# from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer











# @api_view(['POST'])
# def add_user(request):
#    print(request.data)
#    user = serializers.UserSerializer(data={**request.data,})
#    if user.is_valid():
#       user.create(user.data)
#       return Response({"message": "Created!", "data": {}},status.HTTP_201_CREATED)
#    return Response({"message": "Invalid Data"},status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def get_user(request):
   
#    user = models.User.objects.all()
#    print(user)

#    user = serializers.UserSerializer(data=user,many=True)
#    print(user)

#    return Response({"message": "Created!", "data": user},status.HTTP_200_OK)