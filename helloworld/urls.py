from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('alexa', views.alexa, name='alexa'),
    path('signup', views.signup, name='signup')
]