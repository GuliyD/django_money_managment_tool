from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


User = get_user_model()


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            elif len(password) < 6:
                return Response({'error: Password must be at lest 6 characters'})
            else:
                user = User.objects.create_user(email=email, name=name, password=password)
                user.save()
                return Response({'success': 'User created successfully'})
        else:
            return Response({'error': 'Passwords od not match'})


class LogoutView(APIView):
    def post(self, request):
        try:
            print(1)
            refresh_token = request.data["refresh_token"]
            print(2)
            token = RefreshToken(refresh_token)
            print(3)
            token.blacklist()
            print(4)
            return Response({'success': '205'})
        except Exception as e:
            return Response({'error': '400'})