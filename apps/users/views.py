from rest_framework import generics
from rest_framework.permissions import AllowAny

from django.contrib.auth import get_user_model
from apps.users.serializers import SignupSerializer, UserSerializer

User = get_user_model()


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = (AllowAny,)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
