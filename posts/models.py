from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=50)
    header = models.CharField(max_length=120)
    body   = models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.DO_NOTHING,related_name="posts")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    strike = models.BooleanField(default=False)
    published = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images/", blank=True,null=True)
    def __str__(self):
        return self.title

    def formatted_date(self):
        return self.published.strftime("%-d-%-m-%Y %H:%M")

    class Meta:
        ordering = ['-published']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField(default="")
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

class Likes(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="likesmodel")
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="likers")

class Dislikes(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="dislikesmodel")
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="dislikers")
