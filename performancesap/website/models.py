from django.db import models
from performancesap.core.models import CoreModel


# Create your models here.
# MVC - Model View Controler

class ContactM(CoreModel):
	title = models.CharField(max_length=120)
	content = models.TextField(blank=True)
	comment_enabled = models.BooleanField(default=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

class FinanceM(CoreModel):
	stock = models.CharField(max_length=8)
	stock_txt = models.CharField(max_length=90)
	stock_value = models.DecimalField(max_digits=10, decimal_places=4)
	qntity = models.DecimalField(max_digits=10, decimal_places=4)





