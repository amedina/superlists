from django.db import models

class List(models.Model):
	pass
	#id = models.PositiveIntegerField(primary_key=True)

# Create your models here.
class Item(models.Model):
	text = models.TextField(default='')
	list = models.ForeignKey(List, default=None)

	def str(self):
		print('Item: {0}'.format(self.text))
