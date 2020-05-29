from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
	pass

class User(AbstractBaseUser):
	userId = models.AutoField(auto_created=True, primary_key=True, editable=False)
	name = models.CharField(max_length = 255)
	email = models.EmailField(unique = True)
	password = models.CharField(max_length = 255)
	balance = models.IntegerField(blank = True, null = True)
	photo = models.ImageField(upload_to='photos', max_length=255, blank=True, null=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	username = None

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = UserManager()

	def __str__(self):
		return str(self.userId) + ' - ' + self.name

	def check_password(self, passwd):
		if (self.password == passwd):
			return True
		return False