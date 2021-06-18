from django.db import models

# Create your models here.
class Game(models.Model):

    # Note that the primary key is automatically id. so is the db_column
    name = models.CharField(max_length=150)


class Player(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Playthrough(models.Model):
    """
    Relationship table specifying:
    - which game was played
    - by which player
    - was that player a winner or not
    - what was the score of that player in that game

    """

    LOWEST_RATING = 1
    HIGHEST_RATING = 5

    RATING_CHOICES = list(zip(range(LOWEST_RATING, HIGHEST_RATING+1)
                              ,range(LOWEST_RATING, HIGHEST_RATING+1)))

    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    date_started = models.DateTimeField(blank=True, null=True)
    date_ended = models.DateTimeField(blank=True, null=True)
    location = models.CharField(blank=True, max_length=200, null=True)
    winner = models.NullBooleanField(null=True)
    score = models.IntegerField(blank=True, null=True)
    rating = models.IntegerField(choices = RATING_CHOICES, blank=True, null=True)
