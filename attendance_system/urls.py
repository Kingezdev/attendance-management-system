from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from attendance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.record_attendance, name='attendance'),  # Root URL goes to record_attendance
    path('login/', auth_views.LoginView.as_view(template_name='attendance/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('attendance/', include(('attendance.urls', 'attendance'), namespace='attendance')),  # Include other attendance URLs
    path('download/', views.download_attendance, name='download_attendance'),  # Download attendance route
    path('menu/', views.menu, name='menu'),
]
