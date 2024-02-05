from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User, Carts
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'gender', 'age', 'nickname']

class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(required=True)
    age = serializers.CharField(required=True)
    gender = serializers.CharField(required=True)
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'nickname': self.validated_data.get('nickname', ''),
        'age': self.validated_data.get('age', ''),
        'gender': self.validated_data.get('gender', ''),
        }
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user

class CartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carts
        fields = '__all__'
        read_only_fields = ('user', )