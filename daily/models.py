from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.forms.fields import ImageField
from PIL import Image



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.title