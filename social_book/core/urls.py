from operator import index
from django.urls import path
from . import views

urlpatterns = [

path('', views.index, name= "index"),
path('setting', views.setting, name= "setting"),
path('signup', views.signup, name= "signup"),
path('signin', views.signin, name= "signin"),
path('signout', views.signout, name= "signout")

]