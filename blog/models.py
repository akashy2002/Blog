from django.db import models

# Create your models here.


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField(default=0)
    msg = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, null=True)
    slug = models.SlugField(
        unique=True, auto_created=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.message
