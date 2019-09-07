from django.contrib.auth import User
from rest_framerwork.viewsets import ModelViewSet
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    http_method_name = ['post', 'patch']
    serializer_class = UserSerializer