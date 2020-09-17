from django.db import models
from django.urls import reverse
from datetime import date

LENGTH = (
    ('1', '1 hour'),
    ('2', '2 hours'),
    ('3', '3 hours'),
    ('4', '4 hours'),
    ('5', '5 hours'),
    ('6', '6 hours'),
    ('7', '7 hours'),
    ('8', '8 hours'),
    ('9', '9 hours'),
)

# Create your models here.
class VoiceActor(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('voice_actors_detail', kwargs={"pk": self.id})
    

class Game(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    release_year = models.IntegerField()
    voice_actors = models.ManyToManyField(VoiceActor)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'game_id': self.id})
    
    def played_today(self):
        return self.playtime_set.filter(last_played=date.today()).count() >= 1


class Playtime(models.Model):
    last_played = models.DateField()
    length = models.CharField(
        max_length=1,
        choices=LENGTH,
        default=LENGTH[0][0]
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_length_display()} on {self.last_played}"

    class Meta:
        ordering = ['-last_played']