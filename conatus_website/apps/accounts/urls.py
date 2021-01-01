from django.contrib.auth import views as auth_views
from django.urls import path

from .views import ProfileView

app_name = 'accounts'
urlpatterns = [
    # Django Auth stuff
    # path('accounts/', include('django.contrib.auth'))
    path('profile', ProfileView.as_view(), name='profile'),
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
