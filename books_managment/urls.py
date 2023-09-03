from django.urls import path
from . import views

urlpatterns = [
    path('',views.templat,name='template_managment' )
]
