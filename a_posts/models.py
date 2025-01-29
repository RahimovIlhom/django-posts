import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    image = models.URLField(max_length=500)
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name='liked_posts')
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at', )


class Tag(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField(upload_to='icons/', null=True, blank=True)
    slug = models.SlugField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    likes = models.ManyToManyField(User, related_name='liked_comments')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f"{self.author.username}: {self.body[:30]}"
        except:
            return f"No auhtor: {self.body[:30]}"

    class Meta:
        ordering = ['-created']


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='replies')
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.CharField(max_length=150)
    likes = models.ManyToManyField(User, related_name='liked_replies')
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f"{self.author.username}: {self.body[:30]}"
        except:
            return f"No auhtor: {self.body[:30]}"

    class Meta:
        ordering = ['-created']
