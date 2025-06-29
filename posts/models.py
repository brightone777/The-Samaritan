from django.db import models


class Post(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    blocked = models.BooleanField(default=False)
    user = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.content[:50]
