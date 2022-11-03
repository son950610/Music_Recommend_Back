from django.db import models

# Create your models here.






class Song(models.Model):
    class Meta: 
        db_table = 'song'
        
    year = models.CharField(max_length=70, blank=True)
    rank = models.CharField(max_length=70, blank=True)
    title = models.CharField(max_length=70, blank=True)
    genre = models.CharField(max_length=70, blank=True)
    singer = models.CharField(max_length=70, blank=True)
    type = models.CharField(max_length=70, blank=True)
    lyrics = models.TextField(blank=True)
    likes = models.IntegerField(blank=True)
    image = models.TextField(blank=True)
    genre_no = models.IntegerField(blank=True)


