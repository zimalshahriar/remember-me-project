"""remember_me URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from remember import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    #remember
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.createremember, name='createremember'),
    path('current/', views.currentremember, name='currentremember'),
    path('completed/', views.completedremember, name='completedremember'),
    path('remember/<int:remember_pk>', views.viewremember, name='viewremember'),
    path('remember/<int:remember_pk>/complete', views.completeremember, name='completeremember'),
    path('remember/<int:remember_pk>/delete', views.deleteremember, name='deleteremember'),
]
