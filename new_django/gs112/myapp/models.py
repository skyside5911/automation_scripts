from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name=models.CharField(max_length=70)
    song_duration=models.IntegerField()
    def written_by(self):
        return ",".join([str(p) for p in self.user.all()])