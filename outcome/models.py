from django.db import models
from user.models import User

class Outcome(models.Model):
	outcomeId = models.AutoField(auto_created=True, primary_key=True, editable=False)
	name = models.CharField(max_length = 255)
	category = models.CharField(max_length = 255)
	amount = models.IntegerField()
	date = models.DateTimeField(blank = True, null = True)
	isPlan = models.BooleanField(default = False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


	def __str__(self):
		return self.name
