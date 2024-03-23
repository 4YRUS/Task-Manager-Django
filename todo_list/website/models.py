from django.db import models



class record(models.Model):
	create_at=models.DateTimeField(auto_now_add=True)
	task=models.CharField(max_length=200)
	status=models.CharField(max_length=200,default='TODO')


	def __str__(self):
		return self.task