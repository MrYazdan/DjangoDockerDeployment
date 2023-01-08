from api.serializers import UserSerializer, User
from rest_framework.viewsets import ModelViewSet


class UserAPIView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
