from django.urls import path
from . import views

urlpatterns = [
    path('index_page/',views.index_page),
   # path('register/',views.register,name='register'),
    path('subscribe/', views.subscribe, name = 'subscribe'),
]