from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator

# Create your models here.
class Score(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    score = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-name']
