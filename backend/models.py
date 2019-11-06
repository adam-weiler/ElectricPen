from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (MinLengthValidator,)


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(
        validators=[MinLengthValidator(1)]
    )
    draft = models.BooleanField(default=False)    
    published_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    # image = models.FilePathField(path="/img")

    topics = models.ManyToManyField('Topic', related_name='articles')

    # author = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"'{self.title}' - by {self.user}'"


class Topic(models.Model):
    topic = models.CharField(max_length=255)
    # article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return f"topic = {self.topic}"


class Comment(models.Model):
    author = models.CharField(max_length=255)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return f'\'{self.message}\' - {self.author}'
