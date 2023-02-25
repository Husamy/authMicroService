from django.urls import path
from .views import CustomUserApi, PersonalUserAPI
from .views import UserLoginView, UserLogoutView


urlpatterns = [
    path('users/<int:pk>', PersonalUserAPI.as_view()),
    path('users/', CustomUserApi.as_view()),
    path('api/login/', UserLoginView.as_view()),
    path('api/logout/', UserLogoutView.as_view()),

]