from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


class Post(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='post_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    context = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class PostImage(models.Model):
    image = models.ImageField(upload_to='images', blank=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='images')
