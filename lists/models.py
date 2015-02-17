from django.db import models

# Create your models here.
class Item(models.Model):
	text = models.TextField(default='')

	def str(self):
		print('Item: {0}'.format(self.text))