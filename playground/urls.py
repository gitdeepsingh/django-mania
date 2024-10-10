from django.urls import path
from . import views

'''
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
'''
# URLConf: keyword!!, django looks for the word urlpatterns
urlpatterns = [
    path('hello/', views.say_hello) # always end routes with /
] 