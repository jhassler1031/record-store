from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

#User Model
class User(AbstractUser):
    pass

#Band Model - Has many Albums
class Band(models.Model):
    band_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    city_origin = models.CharField(max_length=255, null=True)
    year_formed = models.CharField(max_length=4, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def albums(self):
        from record_app.serializers import AlbumSerializer

        serialized_albums = AlbumSerializer(self.album_set, many=True)
        return serialized_albums.data

    def __str__(self):
        return self.band_name

#Album Model - belongs to Band, has many Tracks
class Album(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, null=True)
    release_year = models.CharField(max_length=4, null=True)
    notes = models.TextField(null=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def tracks(self):
        from record_app.serializers import TrackSerializer

        serialized_tracks = TrackSerializer(self.track_set, many=True)
        return serialized_tracks.data

    def __str__(self):
        return self.title

#Track Mode - belongs to Album
class Track(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        
