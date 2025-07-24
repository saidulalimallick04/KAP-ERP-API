
from django.urls import path
from .views import *
from Users.views import LoginAPI, RegisterAPI, ProfileAPI


urlpatterns = [
    
    
    path('users/login/',LoginAPI.as_view()),
    path('users/register/',RegisterAPI.as_view()),
    
    path('users/profile/',ProfileAPI.as_view()),
    
    path('forms/wheel-specifications',Wheel_Specifications.as_view(), name='Wheel_Specifications'),
    path('forms/bogie-checksheet',Bogie_Checksheet.as_view(), name='Bogie_Checksheet')
]

