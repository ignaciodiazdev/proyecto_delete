
from . import views
from django.urls import path
app_name = "cliente"

urlpatterns = [
    path('', views.home, name="home")
]
