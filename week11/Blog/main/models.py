from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class PostManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    objects = PostManager()

    def to_json(self):
        return {
            'title':self.title,
            'content':self.content,
            'date':self.date,
        }



class Comment(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def to_json(self):
        return {
            'content':self.content,
            'date':self.date
        }
