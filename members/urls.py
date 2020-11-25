from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/',userRegisterView.as_view(),name="register"),
    path('profile/edit/<int:pk>/',editProfilePage.as_view(),name="edit_profile"),
]