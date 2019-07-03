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
    slug = models.SlugField(max_length=50)
    strike = models.BooleanField(default=False)
    published = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def formatted_date(self):
        return self.published.strftime("%-d-%-m-%Y %H:%M")

    class Meta:
        ordering = ['-published']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pass

