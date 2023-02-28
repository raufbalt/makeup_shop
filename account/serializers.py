from rest_framework import serializers
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    password2 = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    word = serializers.CharField(min_length=4, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'word', 'password', 'password2')

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        word = attrs.pop('word')
        if word != 'Rose':
            raise serializers.ValidationError('Вы ввели неверное слово!')
        if attrs['password'] != password2:
            raise serializers.ValidationError('Пароли не совпадают!')
        if attrs['password'].isalpha():
            raise serializers.ValidationError('Пароль должен содержать в себе буквы и цифры. Минимальная длина - 8 знаков.')
        if attrs['password'].isdigit():
            raise serializers.ValidationError('Пароль должен содержать в себе буквы и цифры. Минимальная длина - 8 знаков.')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {'Bad token': _('Token is invalid or expired!')}

    def validate(self, attrs):
        self.token  = attrs['refresh']

        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')