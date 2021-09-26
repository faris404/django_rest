# from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework.authentication import SessionAuthentication

from .serializers import UserSerializer
from .models import User

# Create your views here.

@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This will be `/api/set-csrf-cookie/` on `urls.py`
    """
    return JsonResponse({"details": "CSRF cookie set"})

class UserList(generics.ListCreateAPIView):
    authentication_classes = []
    permission_classes = [] 

    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserLogin(APIView):
    authentication_classes = []
    permission_classes = [] 

    def post(self,request):


        data = request.data
        email = data.get('email')
        password = data.get('password')
        print(email,password)
        if email is None or password is None:
            print('111111')
            return JsonResponse({
                "errors": {
                    "__all__": "Please enter both username and password"
                }
            }, status=400)
        user = authenticate(request,email=email, password=password)
        print(user)
        if user is not None:
            print(222222222)
            login(request, user)
            return JsonResponse({"detail": "Success"})
        return JsonResponse(
            {"detail": "Invalid credentials"},
            status=400,
        )


class UserLogout(APIView):
    authentication_classes = [SessionAuthentication]

    def post(self,request):
        logout(request)
        return JsonResponse({"detail": "Success"})


class UserTest(APIView):

    authentication_classes = [SessionAuthentication]
    def post(self,request):
        print(request.user)
        print(request.user.has_perm('users.view_user'))
        return JsonResponse({"detail": "Success"})
  



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