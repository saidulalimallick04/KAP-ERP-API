from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token

from .serializers import UserRegisterSerializer, LoginSerializer, UserSerializer


class LoginAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        data = request.data
        Ser_data = LoginSerializer(data = data) # Checks if the inputs are valid or not.
        
        if not Ser_data.is_valid():
            content = data.errors
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)   # return if Invalid data
        
        phone = data['phone']
        password = data['password']
        user = authenticate(phone_number = phone, password = password)  # Try to find user/login
        if user is None:
            content={
                'message':'User with mobile number not exist!'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED) # return if no user found.
        
        serialized_user = UserSerializer(user)
        token, _ = Token.objects.get_or_create(user=user)   # Create or fetch the token of corrosponding user.
        
        content = serialized_user.data
        content["access_token"] = str(token)   # Send token to front end.(Issue in frontend: token -> in flatter/access_token -> in deployed server)
        
        return Response(content, status=status.HTTP_200_OK) # Successfull Responce.
    


class RegisterAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        
        serialized_data = UserRegisterSerializer(data= data)    # Checks if the data is valid or not.
        
        if not serialized_data.is_valid():
            content = serialized_data.errors
            return Response(content, status=status.HTTP_400_BAD_REQUEST)    # return error, if invalid input data.
        
        user = serialized_data.save()   # If valid data then create a new user.
        
        token, _ = Token.objects.get_or_create(user=user)   # create a new token for user.
    
        serialized_user = UserSerializer(user)    
        content = serialized_user.data
        content["access_token"] = str(token)   # auto login during registration.
        
        return Response(content, status=status.HTTP_200_OK)
    
    
    
class ProfileAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        current_user = UserSerializer(request.user)
        
        return Response(current_user.data, status=status.HTTP_200_OK)