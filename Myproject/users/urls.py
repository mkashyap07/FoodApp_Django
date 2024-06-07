from django.urls import path

from . import views
app_name='users'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('success/',views.success,name='success'),
    path('profile/',views.profile,name='profile'),

]