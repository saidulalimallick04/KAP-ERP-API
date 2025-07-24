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
        
        print(data)
        Ser_data = LoginSerializer(data = data)
        
        if not Ser_data.is_valid():
            content = data.errors
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        
        phone = data['phone']
        password = data['password']
        user = authenticate(phone_number = phone, password = password)
        if user is None:
            content={
                'response':'Invalid Details'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        
        serialized_user = UserSerializer(user)
        token, _ = Token.objects.get_or_create(user=user)
        
        content = serialized_user.data
        content["token"] = str(token)
        
        return Response(content, status=status.HTTP_200_OK)
    


class RegisterAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        data = request.data
        
        serialized_data = UserRegisterSerializer(data= data)
        
        if not serialized_data.is_valid():
            content = serialized_data.errors
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        
        user = serialized_data.save()
        
        token, _ = Token.objects.get_or_create(user=user)
    
        serialized_user = UserSerializer(user)    
        content = serialized_user.data
        content["token"] = str(token)
        
        return Response(content, status=status.HTTP_200_OK)
    
    
    
    
    
    
class ProfileAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        current_user = UserSerializer(request.user)
        
        return Response(current_user.data, status=status.HTTP_200_OK)