from django.urls import path
from . import views

app_name = 'frequentlyasked'

urlpatterns = [
    path('', views.frequentlyasked, name='frequentlyasked')
]