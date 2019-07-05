from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import (PostsSerializer,CommentSerializer)
from .models import (Post,Comment,Likes,Dislikes)

class Posts(APIView):

    permission_classes = (IsAuthenticated,)

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

@api_view(['POST'])
def like_post(request,post_id,format=None):

    permission_classes = (IsAuthenticated,)

    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        user = request.user

        if Likes.objects.filter(post=post,user=user).exists():
            return Response({'message': 'juz polubiles'})
        post.likes += 1
        post.save() 

        likes = Likes(post=post,user=user).save()
   
        return Response({'message':'Polajkowales'})

@api_view(['POST'])
def dislike_post(request,post_id,format=None):

    permission_classes = (IsAuthenticated,)

    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        user = request.user

        if Dislikes.objects.filter(post=post,user=user).exists():
            return Response({'message': 'juz  zminusowales'})

        if Likes.objects.filter(post=post,user=user).exists():
            return Response({'message': 'obecnie lubisz to'})    
        post.dislikes += 1
        post.save() 

        likes = Dislikes(post=post,user=user).save()
   
        return Response({'message':'Zminusowales'})    

class Comments(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request,post_id,format=None):
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments,many=True)

        return Response(serializer.data)

    def post(self,request,post_id,format=None):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'message':'dodano komentarz'})
        else:
             return Response({'message':serializer.errors})

class CommentDetail(APIView):

    permission_classes = (IsAuthenticated,)

    def put(self,request,post_id,comment_id,format=None):
        post = Post.objects.get(id=post_id)
        comments = Comment.objects.get(id=comment_id)

        serializer = CommentSerializer(comments,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({'message': 'zaktualizowano komentarz'})
        else:
            return Response({'message': serializer.errors})

    def delete(self,request,post_id,comment_id):
        comments = Comment.objects.get(id=comment_id).delete()

        return Response({'message':'usunieto'})
    