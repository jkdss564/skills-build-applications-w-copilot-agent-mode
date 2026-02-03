from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Sample models for demonstration (should be replaced with actual models)
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()
        get_user_model().objects.all().delete()

        # Create teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create users (super heroes)
        ironman = get_user_model().objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        captain = get_user_model().objects.create_user(username='captain', email='captain@marvel.com', password='password', team=marvel)
        batman = get_user_model().objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = get_user_model().objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Create activities
        app_models.Activity.objects.create(user=ironman, type='run', duration=30)
        app_models.Activity.objects.create(user=batman, type='cycle', duration=45)

        # Create leaderboard
        app_models.Leaderboard.objects.create(user=ironman, score=100)
        app_models.Leaderboard.objects.create(user=batman, score=90)

        # Create workouts
        app_models.Workout.objects.create(name='Pushups', description='Do 20 pushups')
        app_models.Workout.objects.create(name='Situps', description='Do 30 situps')

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
