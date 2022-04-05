from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class YesNoForm(forms.Form):
    electric_car = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))
    provider = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))
    reduce_reuse_recycle = forms.TypedChoiceField(coerce=lambda x: x =='True', choices=((False, 'No'), (True, 'Yes')))
    budget = forms.IntegerField(label="budget", min_value=0)