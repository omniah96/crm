from django.shortcuts import render , redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users
from django.contrib import messages
# Create your views here.



@unauthenticated_user
def registerPage(request):

	#rendering the form
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			#flushing success messages when the user is registered
			username = form.cleaned_data.get('username')
			messages.success(request , 'Account was created for' + username)


			#assigning the new user to customer group
			#making the new group = customer then adding this groupName to the user's data
			group = Group.objects.get(name = 'customer')
			user.groups.add(group)

			#creating a customerPage for each new customer
			Customer.objects.create(
				user = user,
				)

			#redirect user to loginPage once he is registered
			return redirect('login')
	context = {'form' : form}
	return render(request , 'accounts/register.html' , context)


@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request , username = username , password = password)

		if user is not None:
			login(request , user)
			return redirect('home')

		else:
			messages.info(request , 'Username or Password is incorrect')

	context = {}
	return render(request , 'accounts/login.html' , context)

def logoutUser(request):

	logout(request)
	return redirect('login')


def home(request):

	customers = Customer.objects.all()
	orders = Order.objects.all()

	orders_count = customers.order_set.all().count()

	total_orders = orders.count()
	delivered = orders.filter(status = 'Delivered').count()
	pending = orders.filter(status = 'Pending').count()


	context = {'customers' : customers ,'orders' : orders , 'orders_count' : orders_count , 'total_orders' : total_orders , 'delivered' : delivered , 'pending' : pending}

	return render(request , 'accounts/dashboard.html' , context)


#@required_login(login_url = 'home')
@allowed_users(allowed_roles = ['customer'])
def userPage(request):

	#the orders for the specific customer user
	orders = request.user.customer.orders_set.all()
	total_orders = orders.count()
	delivered = orders.filter(status = 'Delivered').count()
	pending = orders.filter(status = 'Pending').count()

	context = {'orders' : orders , 'total_orders' : total_orders , 'delivered' : delivered , 'pending' : pending}
	return redirect(request , 'accounts/user.html' , context)

@allowed_users(allowed_roles = ['customer'])
def accountSettings(request):


	customer = request.user.customer
	form = CustomerForm(instatnce = customer)

	if request.method == 'POST':
		#the only different part in handling the submissions of a picture
		form = CustomerForm(request.POST , request.FILES , instance = customer)
		if form.is_valid():
			form.save()
	context = {'form' : form}
	return render(request , 'accounts/account_settings.html' , context)




def products(request):

	products = Product.objects.all()
	context = {'products' : products}

	return render(request , 'accounts/products.html' , context)

def customers(request , pk):

	customers = Customer.objects.get(id = pk)
	orders = customers.order_set.all()
	order_count = orders.count()
	#total_orders = orders.all().count()

	context = {'customers' : customers , 'orders': orders , 'order_count' : order_count}
	return render(request , 'accounts/customers.html' , context)


def createOrder(request):

	form = ModelForm()

	if request.method == 'POST':
		form = ModelForm(request.POST)
		if form.is_valid():
			form.save()

			return redirect('/')
	context = {'form' : form}


	return render(request , 'accounts/order_form.html' , context)


def updateOrder(reuest , pk):


	order = Order.objects.get(id = pk)
	form = OredrForm(instance = order)

	if request.method == 'POST':
		form = OredrForm(request.method , instance = order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form' : form}

	return render(request , 'accounts/order_form.html' , context)


def deleteOrder(request , pk):
	order = Order.objects.get(id , pk)
	if request.method == 'POST':
		order.delete()
		return redirect('/')

	context = {'order' : order}

	return render(request , 'accounts/delete_order' , context)




















