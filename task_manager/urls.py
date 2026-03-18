from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from task_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('task_manager.users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('tasks/', include('task_manager.tasks.urls')),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('statuses/', include('task_manager.statuses.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('', views.home, name='home'),
]