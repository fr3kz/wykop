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

    def post(self,request,format=None):
        serializer = PostsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                'message':'utworzono post',
                'post': serializer.data
            })

        else:
            return Response({'error':'brak wszystkich pol'})

    def put(self,request,format=None):
        post = Post.objects.get(id=request.data['id'])
        print(post)
        serializer = PostsSerializer(post,data=request.data)

        if serializer.is_valid():
            serializer.save(post=post)

            return Response({
                'message':'utworzono post',
                'post': serializer.data
            })

        else:
            return Response(serializer.errors)

    def delete(self,request,format=None):
        post = Post.objects.get(id=request.data['id'])
        post.delete()

        return Response({'message':'post zostal usuniety'})

