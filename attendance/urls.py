from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.record_attendance, name='record_attendance'),
    path('attendance/success/', views.success, name='success'),
    path('attendance/list/', views.list_attendance, name='list_attendance'),  
    path('attendance/login/', auth_views.LoginView.as_view(template_name='attendance/login.html'), name='login'),
    path('attendance/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('attendance/download/', views.download_attendance, name='download_attendance'),  # New download route
]
