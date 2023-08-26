from django.urls import path, include
from . import views


app_name = 'users'
urlpatterns = [
    # include default auth URLS
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]