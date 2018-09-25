from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.title

	@property
	def sayHi(self):
		print('HELLO PEOPLE')
		return 'TEst'
