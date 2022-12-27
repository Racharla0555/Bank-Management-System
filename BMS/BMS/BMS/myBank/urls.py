from django.contrib import admin
from django.urls import path
from myBank import views
urlpatterns = [
    path('',views.home,name='myBank'),
    path("createacc",views.createacc,name='Create Account'),
    path("login/",views.login1,name="Login"),
    path("accounts/login/",views.login1,name="Login"),
    path("options",views.options,name="Options"),
    path("accdetail",views.accdeatils,name="Account Details"),
    path("contactus",views.contactus,name="Contact US"),
    path("resetpin",views.resetpin,name="Reset Pin"),
    path("modifyacc",views.modifyacc,name="Modify Account"),
    path("transaction",views.transaction,name="Transaction")
]
