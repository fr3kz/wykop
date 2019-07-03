from rest_framework.serializers import ModelSerializer
from .models import (Post,Comment)
from django.contrib.auth.models import User

class PostsSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

    def create(self,validated_data):

        user = User.objects.get(id=validated_data['posted_by'])
        
        post = Post(
            title=validated_data['title'],
            header=validated_data['header'],
            body=validated_data['body'],
            posted_by=user,
            slug=validated_data['title']
        )
        post.save()

        return post

    def update():
        pass