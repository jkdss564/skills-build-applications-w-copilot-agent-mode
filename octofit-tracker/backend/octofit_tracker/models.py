from djongo import models
from django.contrib.auth.models import AbstractUser
from bson import ObjectId

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class User(AbstractUser):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, to_field='_id', db_column='team_id')

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='_id', db_column='user_id')
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='_id', db_column='user_id')
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
