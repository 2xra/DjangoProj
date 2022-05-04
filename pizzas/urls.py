from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('',views.homepage, name='homepage'),
]