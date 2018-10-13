from django.db import models
class User(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    content = models.TextField(editable=True)
    date = models.DateField(auto_now=False, editable=True)


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, editable=True)
    posts = models.ForeignKey(Post,on_delete=models.CASCADE)