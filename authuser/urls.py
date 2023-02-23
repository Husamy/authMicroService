from django.urls import path
from .views import CustomUserApi, PersonalUserAPI


urlpatterns = [
    path('users/<int:pk>', PersonalUserAPI.as_view()),
    path('users/', CustomUserApi.as_view())
]