from django.db import models

class Lead(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	email = models.EmailField()
	image = models.ImageField(upload_to='images', blank=True)
	message = models.CharField(max_length=300)
	created_at = models.DateTimeField(auto_now_add=True)

	def get_image(self):
		if self.image:
			return 'https://user-drf.herokuapp.com' + self.image.url
		return ''


	def __str__(self):
		return self.name
