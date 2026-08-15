import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True,primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)

class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reactions")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reactions")

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)