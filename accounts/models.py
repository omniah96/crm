from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):

	#a customer can have only one user and a user can have one customer
	#and whenever that user is deleted , the relationship between him and the customer is deleted
	user = models.OneToOneField(User , null = True , blank = True, on_delete = models.CASCADE)
	name = models.CharField(max_length = 200 , null = True)
	phone = models.CharField(max_length = 200 , null = True)
	email = models.CharField(max_length = 200 , null = True)
	#install pillow before migrating this filed cause images depends on it,then will configure the settingsFile
	#default pic for a new user if he didn't upload one by himself
	profile_pic = models.ImageField(default = "profile1.png" , null = True , blank = True)
	date_created = models.DateTimeField(auto_now_add = True , null = True)

	def __str__(self):

	    return self.name


class Tag(models.Model):

	name  = models.CharField(max_length = 200 , null = True)

	def __str__(self):
		return self.name


class Product(models.Model):

	#DropDown:

	CATEGORY = (

		('Outdoor' , 'Outdoor'),
		('Indoor' , 'Indoor'),


		)

	name = models.CharField(max_length = 200 , null = True)
	price = models.FloatField(max_length = 200 , null = True)

	category = models.CharField(max_length = 200 , null = True , choices = CATEGORY)

	#null is for form submission, we need to make blank equals null also for description
	description = models.CharField(max_length = 200 , null = True , blank = True)
	date_created = models.DateTimeField(auto_now_add = True , null = True)

	#ManyToManyRelationShip

	tags = models.ManyToManyField(Tag)



	
class Order(models.Model):

	#DropDown:

	STATUS = (

		('Pending' , 'Pending'),
		('Out for delivery' , 'Out for delivery'),
		('Delivered' , 'Delivered'),


		)

	#OneToMany Relationship

	customer = models.ForeignKey(Customer , null = True , on_delete = models.SET_NULL)
	product = models.ForeignKey(Product , null = True , on_delete = models.SET_NULL)


	date_created = models.DateTimeField(auto_now_add = True , null = True)
	status = models.CharField(max_length = 200 , null = True , choices = STATUS)












