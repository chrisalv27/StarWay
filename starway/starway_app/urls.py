from django.urls import path
from . import views

app_name = 'starway_app'
urlpatterns = [
    path('', views.myview, name='myview')
]