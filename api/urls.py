
from django.urls import path
from .views import *
from Users.views import LoginAPI, RegisterAPI, ProfileAPI


urlpatterns = [
    path('users/login/',LoginAPI.as_view()), # LOGIN POST
    path('users/register/',RegisterAPI.as_view()), # Register POST
    
    path('users/profile/',ProfileAPI.as_view()),    # Profile data GET
    
    path('forms/wheel-specifications',Wheel_Specifications.as_view(), name='Wheel_Specifications'), # For wheel data GET/POST
    path('forms/bogie-checksheet',Bogie_Checksheet.as_view(), name='Bogie_Checksheet')  # For bogie data GET/POST
]

