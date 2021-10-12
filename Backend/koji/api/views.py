from account.models import UserProfile
from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer


class UserList(ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


