from django.db import models

# Create your models here.



class Genre(models.Model):
    class Meta:
        db_table = 'genre'
    name = models.CharField(max_length=70, default='')




class Song(models.Model):
    class Meta:
        db_table = 'song'
    year = models.CharField(max_length=70, default='')
    rank = models.CharField(max_length=70, default='')
    title = models.CharField(max_length=70, default='')
    genre = models.ManyToManyField(Genre, related_name='songs')
    singer = models.CharField(max_length=70, default='')
    type = models.CharField(max_length=70, default='')
    lyrics = models.TextField(max_length=500, default='')
    likes = models.CharField(max_length=70, default='')
    image = models.TextField(max_length=256, default='')


