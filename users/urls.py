from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import UserCreateView, UserDetailView

app_name = 'users'

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='detail'),
    path('login/', LoginView.as_view(template_name='form.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]