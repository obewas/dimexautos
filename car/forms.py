from django import forms
from .models import *

class CarCreateForm(forms.ModelForm):

	class Meta:
		model = Car
		fields = '__all__'




