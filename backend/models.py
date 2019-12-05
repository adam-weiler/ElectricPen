from django.db import models
from django.contrib.auth.models import User
from django.core.validators import (MinLengthValidator,)


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, related_name='articles')
    
    updated_on = models.DateTimeField(auto_now=True)

    content = models.TextField(
        validators=[MinLengthValidator(1)]
    )

    created_on = models.DateTimeField(auto_now_add=True)

    # image = models.FilePathField(path="/img")

    topics = models.ManyToManyField('Topic', default='Unsorted', related_name='articles')

    # status = models.BooleanField(default=False)
    status = models.IntegerField(choices=((0,"Draft"),(1,"Publish")), default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"'{self.title}' - by {self.owner}'"

    def save(self, *args, **kwargs):
        """
        Save the article.
        """
        super(Article, self).save(*args, **kwargs)

    


class Topic(models.Model):
    topic = models.CharField(max_length=255)
    # article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return f"{self.topic}"


class Comment(models.Model):
    owner = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'\'{self.message}\' - {self.owner}'
