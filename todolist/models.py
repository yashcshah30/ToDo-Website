from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class ToDo(models.Model):
	def validate_date(due_date):
		if due_date.date()<timezone.now().date():
			raise ValidationError("Date cannot be in the past")

	title = models.CharField(max_length=50)
	description = models.TextField()
	due_date = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"), validators=[validate_date])
	date_created = models.DateTimeField(default=timezone.now().strftime("%Y-%m-%d"))
	
