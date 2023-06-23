from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from . models import MyUser
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    country_code = serializers.CharField(max_length=4)
    phone_number = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128)
    password_confirm = serializers.CharField(max_length=128)

    class Meta:
        model = MyUser
        fields = ('country_code', 'phone_number', 'email', 'password', 'password_confirm')

    def create(self, validated_data):
        country_code = validated_data.pop('country_code')
        phone_number = validated_data.pop('phone_number')
        email = validated_data.get('email')

        try:
            existing_user = MyUser.objects.get(email=email)
            return serializers.ValidationError("This email address is already registered.")
        except ObjectDoesNotExist:
            pass

        try:
            existing_user = MyUser.objects.get(country_code=country_code, phone_number=phone_number)
            return serializers.ValidationError("This phone number is already registered.")
        except ObjectDoesNotExist:
            pass

        user = MyUser.objects.create_user(
            country_code=country_code,
            phone_number=phone_number,
            **validated_data
        )

        return user
class LogInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=6, write_only=True)