from django.urls import path
from .views import UserRegisterView, UserUpdateView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register', ),
    path('edit_profile/', UserUpdateView.as_view(), name='edit_profile'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='user_profile'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_user_profile_page/', CreateProfilePageView.as_view(), name='create_user_profile_page'),
]
