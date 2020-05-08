from django.db import models

class User(models.Model):
	userId = models.AutoField(auto_created=True, primary_key=True, editable=False)
	name = models.CharField(max_length = 255)
	email = models.EmailField()
	password = models.CharField(max_length = 255)
	balance = models.IntegerField(blank = True, null = True)
	photo = models.ImageField(upload_to='photos', max_length=255, blank=True, null=True)

	def __str__(self):
		return self.nama