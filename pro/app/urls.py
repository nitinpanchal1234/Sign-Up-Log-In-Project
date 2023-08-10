from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signup_action', views.signup_action, name='signup_action'),
    path('login', views.login, name='login'),
    path('login_action', views.login_action, name='login_action'),
]