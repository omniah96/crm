from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [


    path('register/' , views.registerPage , name = "register"),
    path('login/' , views.loginPage , name = "login"),
    path('logout/' , views.logoutUser , name = "logout"),

    path('userpage/' , views.userPage , name = "userpage"),
    path('account/' , views.accountSettings , name = "account"),

    path('' , views.home , name = "home"),
    path('products/' , views.products , name = "products"),
    path('customers/<str:pk>/' , views.customers , name = "customers"),


    path('create_order/' , views.createOrder , name = "create_order"),
    path('update_order/<str:pk>/' , views.updateOrder , name = "update_order"),
    path('delete_order/<str:pk>/' , views.deleteOrder , name = "delete_order"),

    #resetPassword Views
    path('reset_password/' , 
        auth_views.PasswordResetView.as_view(template_name = "accounts/password_reset.html") , 
        name = "reset_password"),
    path('reset_password_sent/' , 
        auth_views.PasswordResetDoneView.as_view(template_name = "accounts/password_reset_sent.html") , 
        name = "password_reset_done"),
    path('reset / <uidb64>/<token>/' , 
        auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_confirm.html") , 
        name = "password_reset_confirm"),
    path('reset_password_complete/' ,
     auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_done.html") ,
      name = "password_reset_complete") ,

]

#1-Submit email form
#2-Email sent success message
#3-link to password reset form in email
#4-password successfully changed message