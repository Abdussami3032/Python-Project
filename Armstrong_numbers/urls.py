from django.urls import path
from . import views

app_name = 'Armstrong_numbers'

urlpatterns = [
    path('', views.index, name='index'),
]