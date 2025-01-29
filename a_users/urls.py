from django.urls import path

from .views import profile_view, profile_edit_view, delete_profile_view

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', profile_edit_view, name='profile-edit'),
    path('profile/onboarding/', profile_edit_view, name='profile-onboarding'),
    path('profile/delete/', delete_profile_view, name='profile-delete'),
    path('author/profile/<username>/', profile_view, name='author-profile'),
]