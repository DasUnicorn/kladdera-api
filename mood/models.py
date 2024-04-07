from django.db import models
from users.models import CustomUser


class Mood(models.Model):
    MOOD_CHOICES = [
        ('very_happy', 'Very Happy'),
        ('happy', 'Happy'),
        ('neutral', 'Neutral'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('exhausted', 'Exhausted'),
    ]

    date = models.DateField(auto_now_add=True)
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    note = models.TextField(max_length=500,  blank=True)

    def __str__(self):
        return f"{self.user.email}'s mood on {self.date}"
