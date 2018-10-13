from django.db import models
import datetime

now = datetime.datetime.now()
class Posts(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateTimeField(default=now)

class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateTimeField(default=now)
    comment = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments', null=True)

