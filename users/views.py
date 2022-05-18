from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.


class SignUpAuth(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or email == '':
            return Response({"details": "Please enter an email address"}, status=400)

        try:
            user = OkUser.objects.get(email=email)
            if user:
                return Response({"details": "Email address already exist"}, status=400)
        except OkUser.DoesNotExist:
            myuser = OkUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
            )

            myuser.set_password(password)
            myuser.save()
            """Send successfully email creation"""
            return Response({"details": "User successfully created"})
