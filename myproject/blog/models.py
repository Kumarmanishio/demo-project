from django.db import models
from datetime import date
from django.urls import reverse


class Blog(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, help_text="Enter you blog text here.")
    post_date = models.DateField(default=date.today)

    class Meta:
        ordering = ["-post_date"]

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=120, help_text='title of message.')
    message = models.TextField(help_text="what's on your mind ...")
    user = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title