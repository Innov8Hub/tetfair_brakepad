from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('submit_quickrun/', views.submit_data_quickrun, name='submit_data_quickrun'),
]