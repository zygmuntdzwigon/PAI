"""my_e_wallet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_view
from django.urls import path, include
from users import views as user_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('djangoadmin/', admin.site.urls),
    path('', include('debt.urls')),
    path('register/', user_view.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-change/', user_view.pw_change, name='password_change'),
    path('profile/', user_view.profile, name='profile'),
    path('admin/', user_view.UsersListView.as_view(template_name='users/admin.html'), name='admin'),
    path('user/<int:pk>', user_view.UserDetailView.as_view(template_name='users/user_detail.html'), name='user-detail'),
    path('user/<int:pk>/delete/', user_view.UserDeleteView.as_view(template_name='users/user_delete.html'), name='user-delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
