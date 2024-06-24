"""
URL configuration for todo_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from todo.views import todo_form, signup, ToDoListView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'), 
    path('accounts/profile/', RedirectView.as_view(pattern_name='todo_list', permanent=False)), # Root URL mapped to login view
    path('todo_list/', login_required(ToDoListView.as_view()), name='todo_list'),
    path('todo_form/', login_required(todo_form), name='todo_form'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
]

