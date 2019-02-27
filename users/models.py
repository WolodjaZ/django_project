from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	student_email = models.EmailField(max_length=70)
	image = models.ImageField(upload_to='profile_image', blank=True)

	def __str__(self):
		return self.user.username

	def create_profile(sender, **kwargs):
		if kwargs['created'] and kwargs['instance'].userprofile == None:
			user_profile = UserProfile.objects.create(user=kwargs['instance'])

	post_save.connect(create_profile, sender=User)
