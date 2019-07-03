from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (PostsSerializer)
from .models import Post

class Posts(APIView):

    def get(self,request,format=None):

        posts = Post.objects.all()
        serializer = PostsSerializer(posts, many=True)

        return Response({
            'posts':serializer.data
        })