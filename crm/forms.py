from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class = CustomerForm(ModelForm):
#we want the user to edit all the fields except for the user field
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']



class OrderForm(ModelForm):
	class Meta:
		model = Oredr
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	model = User
	fields = ['username' , 'email' , 'password1' , 'password2']