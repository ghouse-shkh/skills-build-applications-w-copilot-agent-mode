from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (Superheroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
        ]

        # Create Activities
        activities = [
            Activity.objects.create(user=users[0], type='Run', duration=30, calories=300),
            Activity.objects.create(user=users[1], type='Swim', duration=45, calories=400),
            Activity.objects.create(user=users[2], type='Bike', duration=60, calories=500),
            Activity.objects.create(user=users[3], type='Yoga', duration=50, calories=200),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', difficulty='Medium'),
            Workout.objects.create(name='Strength Training', description='Strength for all heroes', difficulty='Hard'),
        ]

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=1000)
        Leaderboard.objects.create(user=users[1], score=900)
        Leaderboard.objects.create(user=users[2], score=1100)
        Leaderboard.objects.create(user=users[3], score=950)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
