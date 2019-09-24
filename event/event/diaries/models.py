from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=250,unique=True)
    # image = models.ImageField(upload_to="category/%y/%m",blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class Album(models.Model):
    category = models.ForeignKey(Category,related_name="category",on_delete=models.CASCADE)

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to="albumCover/%y/%m", blank=False)
    location = models.CharField(max_length=250,blank=True)
    show = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.name)

class AlbumImage(models.Model):
    album = models.ForeignKey(Album,related_name="album",on_delete=models.CASCADE)
    images = models.ImageField(upload_to="Images/%y/%m/%d",blank=False)