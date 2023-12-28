from django.db import models
from post.models import Post

# Create your models here.

class Like(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='like',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'auth.User',
        related_name='like',
        on_delete=models.CASCADE
    )
