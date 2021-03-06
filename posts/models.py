from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True, related_name="comments")
	content = models.TextField(null=True)
	image = models.ImageField(blank=True, upload_to='post_images')
	likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.author.username} - {self.date_posted} Post' 