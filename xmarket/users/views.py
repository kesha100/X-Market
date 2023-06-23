from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import MyUser
from .serializers import RegisterSerializer, LogInSerializer
from .sms_utils import send_verification_code, generate_verification_code


# Create your views here.



class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        verification_code = generate_verification_code()
        send_verification_code(MyUser.full_phone_number, verification_code)
        if serializer.is_valid(raise_exception=True):
            return Response('Вы успешно зарегистрировались', status=status.HTTP_201_CREATED)


def get_login_response(user, request):
    refresh = RefreshToken.for_user(user)
    data = {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token)
    }


class LogInAPIView(generics.GenericAPIView):
    serializer_class = LogInSerializer
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'],
                            password=serializer.validated_data['password'])
        if not user:
            raise exceptions.AuthenticationFailed
        login(request, user)
        return Response(data=get_login_response(user, request))


def index(request):
    return HttpResponse("Hello, World!")