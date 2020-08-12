from django import forms
from .models import ToDo
from bootstrap_datepicker_plus import DatePickerInput

class ReminderForm(forms.ModelForm):
	class Meta:
		model = ToDo
		fields = ['title', 'description', 'due_date']
		widgets = {
            'due_date': DatePickerInput(
                options={
                    "format": "MM/DD/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
            ),
        }