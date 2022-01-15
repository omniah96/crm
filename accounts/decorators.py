from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
	def wrapper_func(request , *args , **kwargs):
		if request.user.is_authenticated:
			#if authenticated never call the loginPage and redirect him to homePage
			return redirect('home')
		else:
			#if not authenticated let the original process(registeration or login process begins)
			return view_func(request , *args , **kwargs)
	return wrapper_func


# 3 layers function
def allowed_users(allowed_roles = []):
	def decorator(view_func):
		def wrapper_func(request , *args , **kwargs):
			goroup = None
			if request.user.group.exists():
				group = request.user.groups.all()[0]
				if group in allowed_roles:
					return view_func(request , *args , **kwargs)
				else:
					return HttpResponse('You are not allowed to view this page')
		return wrapper_func
	return decorator


def admin_only(view_func):
	def wrapper_func(request , *args , **kwargs):

		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

			if group == 'customer':
				return redirect('user-page')
			if group == 'admin':
				return view_func(request , *args , **kwargs)

	return wrapper_func
