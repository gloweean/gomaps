from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

__all__ = [
    'UserSerializer',
    'UserCreateSerializer',
]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'gender',
            'phone_num',
            'birthday',
            'last_login',
            'date_joined',
        ]
        read_only_fields = [
            'id',
            'username',
            'email',
            'last_login',
            'date_joined',
        ]
        

class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False, allow_null=False)
    email = serializers.EmailField()
    name = serializers.CharField(allow_blank=False, allow_null=False)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, username):
        if User.object.filter(username=username).exists():
            raise serializers.ValidationError('This Username already exist')
        return username

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError('Passwords didn\'t match')
        return data

    def save(self, *args, **kwargs):
        username = self.validated_data.get('username', '')
        name = self.validated_data.get('name', '')
        email = self.validated_data.get('email', '')
        password = self.validated_data.get('password1', '')
        user = User.object.create_user(
            username=username,
            name=name,
            email=email,
            password=password,
        )
        return user