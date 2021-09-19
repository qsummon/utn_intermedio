"""utn_intermedio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('lab/', include('lab.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from django.urls import include
from django.conf.urls import include
from users import views as user_views

urlpatterns = [
    url('admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url('register/', user_views.register, name='register'),
    url('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    url('', include('lab.urls')),
]
