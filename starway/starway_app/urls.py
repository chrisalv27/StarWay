from django.urls import path
from . import views

app_name = 'starway_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('getsign', views.getsign, name='getsign')
]