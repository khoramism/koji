from account.models import UserProfile
from rest_framework.generics import DestroyAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView , RetrieveUpdateAPIView
from .serializers import UserSerializer


class UserList(ListCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    """
    API endpoint that view a user details.
    """

    serializer_class = UserSerializer
    lookup_field = "email"

    def get_queryset(self):
        return UserProfile.objects.filter(email=self.kwargs['email'])


class UserDelete(DestroyAPIView):
    """
    API endpoint that Delete a user.
    """

    serializer_class = UserSerializer
    lookup_field = "email"

    def get_queryset(self):
        return UserProfile.objects.filter(email=self.kwargs['email'])


class UserCreate(CreateAPIView):
    """
    API endpoint that Create a user.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    lookup_field = "email"


class UserUpdate(RetrieveUpdateAPIView):
    """
    API endpoint that Update a user information.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    lookup_field = "email"
