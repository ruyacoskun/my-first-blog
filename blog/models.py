from django.db import models
from django.utils import timezone


class Post(models.Model):
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilis_tarihi = models.DateTimeField(
            default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(
            blank=True, null=True)

    def yayinla(self):
        print(self)
        self.yayinlanma_tarihi = timezone.now()
        print(self)
        print(self.yayinlanma_tarihi)
        self.save()

    def __str__(self):
        return self.baslik

    def approved_comments(self):
    	return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

  
# Create your models here.
