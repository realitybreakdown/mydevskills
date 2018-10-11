from django.db import models
from django.contrib.auth.models import User

# Create your models here.

LEVELS = (
    (1, 'Fundamental Awareness'),
    (2, 'Novice'),
    (3, 'Intermediate'),
    (4, 'Advanced'),
    (5, 'Expert'),
)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250) 
    levels = models.CharField(
       max_length=1,
       # add the 'choices' field option
       choices=LEVELS,
       # set the default value for meal to be 'B'
       default=LEVELS[0][0])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

