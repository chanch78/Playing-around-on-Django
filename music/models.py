from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
# When Create each class would give it a primary key
# Have to figure how to save the entire conversation
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(default=0)
    is_favorite = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    # this function makes a string representation of the object
    def __str__(self):
        return self.album_title + ' - ' + self.artist

# on_delete=model.CASCADE <Not a must>
# whenever we delete an album, any song that is link to the album will be deleted
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title