from rest_framework import serializers


from .models import User


class LoginSerializer(serializers.Serializer):
    
    phone = serializers.CharField()
    password = serializers.CharField()


class UserRegisterSerializer(serializers.Serializer):
    
    user_type = serializers.CharField()
    phone_number = serializers.CharField()
    whatsapp_number = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        if User.objects.filter(phone_number = data['phone_number']).exists():
            raise serializers.ValidationError(detail = 'Phone Number is already Used!!')
        
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError('Email Address is already Used!!')

        return data
    def create(self, validated_data):
        new_user = User()
        new_user.phone_number = validated_data['phone_number']
        new_user.whatsapp_number = validated_data['whatsapp_number']
        new_user.user_type = validated_data['user_type']
        new_user.first_name = validated_data['first_name']
        new_user.last_name = validated_data['last_name']
        new_user.username = f"{validated_data['first_name']}_{validated_data['phone_number']}_"
        new_user.email = validated_data['email']
        
        new_user.set_password(validated_data['password'])
        new_user.save()
        
        return new_user
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        
        fields = ["id",
                "username",
                "user_type",
                "phone_number",
                "whatsapp_number",
                "first_name",
                "middle_name",
                "last_name",
                "email",
                "created_at",
                "secondary_phone"
            ]
        
        