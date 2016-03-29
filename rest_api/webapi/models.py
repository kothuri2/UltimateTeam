from django.db import models

# Create your models here.
class Team(models.Model):
	team_name = models.CharField(max_length=100, null=True)
	manager = models.CharField(max_length=100, null=True)
	league = models.CharField(max_length=100, null=True)
	location = models.CharField(max_length=100, null=True)
	team_titles = models.IntegerField(default=0, null=True)

	# For printing string
	def __str__(self):
		return self.team_name

	# Has won any titles
	def has_won_titles(self):
		return self.team_titles > 0

class Player(models.Model):
	player_name = models.CharField(max_length=100, null=True)
	position = models.CharField(max_length=3, null=True)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
	nationality = models.CharField(max_length=100, null=True)
	player_league = models.CharField(max_length=100, null=True)

	class Meta:
		ordering = ["player_name"]

	def __str__(self):
		return self.player_name