from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200,)
	content = models.TextField(blank=True,)
	image = models.ImageField(upload_to='imgs', null=True,)
	class Draft(models.IntegerChoices):
		NO = 0
		YES = 1
		__empty__ = 0
	draft = models.IntegerField(choices=Draft.choices)
	# auto fill
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,)
	created_date = models.DateTimeField(default=timezone.now, null=True,)

	def publish(self):
		self.created_date = timezone.now()
		self.save()

	def draft(self):
		self.created_date = None
		self.save()

	def __str__(self):
		return self.title
