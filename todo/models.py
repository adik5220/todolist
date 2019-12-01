from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.urls import reverse

class Category(models.Model):
	name = models.CharField(default="general", max_length=100)

	class Meta:
		verbose_name = ("Категория")
		verbose_name_plural = ("Категории")

	def __str__(self):
		return self.name

class TodoList(models.Model): 
	title = models.CharField(max_length=250)
	content = models.TextField(blank=True)
	created = models.DateField(default=timezone.now(), null=True)
	due_date = models.DateField(default=timezone.now()+timedelta(days=3), null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default="general")
	picture = models.ImageField(upload_to='static/picture/', blank=True, default='static/picture/No_image_3x4.svg.png')

	def get_absolute_url(self):
		return reverse('det', args=[int(self.id)])

	def __str__(self):
		return self.title

# Create your models here.
