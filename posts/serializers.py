from rest_framework.serializers import ModelSerializer
from .models import (Post,Comment)
from django.contrib.auth.models import User

class PostsSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def create(self,validated_data):

        post = Post(
            title=validated_data['title'],
            header=validated_data['header'],
            body=validated_data['body'],
            posted_by=validated_data['posted_by'],
        )
        post.save()

        return post

    def update(self,post,validated_data):

        title = validated_data['title']
        header = validated_data['header']
        body = validated_data['body']
        posted_by = validated_data['posted_by']

        post.title = title
        post.header = header
        post.body = body
        post.posted_by = posted_by
        
        post.save()
        
        return post