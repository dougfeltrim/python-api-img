
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from users import views as user_views
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('upload/', views.upload_resume, name='upload'),
        
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]