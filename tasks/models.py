from django.db import models
from users.models import CustomUser


class Task(models.Model):
    TASK_FREQUENCY_CHOICES = [
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    ]

    title = models.CharField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    energy_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_repeating = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=1, choices=TASK_FREQUENCY_CHOICES, null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(energy_level__gte=1) & models.Q(energy_level__lte=10),
                name="energy_level_between_1_and_10",
            )
        ]

    def __str__(self):
        return self.title
