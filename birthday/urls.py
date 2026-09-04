from django.urls import path
from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.login, name='login'),
    path('welcome/', views.landing, name='landing'),
    path('main/', views.main, name='main'),
    path('logout/', views.logout, name='logout'),
]
