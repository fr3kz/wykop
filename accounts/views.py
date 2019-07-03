from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib import auth
from .serializer import UserSerializer

class SignIn(APIView):

    def post(self,request,format=None):

        username = request.data['username']
        password = request.data['password']

        user = auth.authenticate(request,username=username, password=password)

        if user is not None:
           refresh = RefreshToken.for_user(user)

           context = {
               'access': str(refresh.access_token)
           }

           return Response(context)
           
        return Response({'error':'Zle dane'})

class SignUp(APIView):

    def post(self,request,format=None):

        username = request.data['username']
        password = request.data['password']

        user = auth.authenticate(request,username=username, password=password)

        if user is None:
      
            usr = User.objects.create_user(username=username,password=password)
            token = RefreshToken.for_user(usr)

            return Response({
                'access':str(token.access_token),
                'user_id': usr.id
                })
        else:
            return Response({'error': ' nick jest zajety'})

class Users(APIView):

    def get(self,request,format=None):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)

        return Response({'users':serializer.data})