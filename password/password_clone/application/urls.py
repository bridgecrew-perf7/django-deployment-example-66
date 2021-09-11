from django.conf import urls
from django.conf.urls import url
from application import views

app_name = 'application'

urlpatterns = [
    url('register/', views.registration, name='register'),
    url('user_login', views.user_login, name='user_login'),
]