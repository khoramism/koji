from team.models import Team
from event.models import Event
from rest_framework.generics import DestroyAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from ..serializers.TeamSerializers import TeamSerializer, TeamCreateSerializer, TeamEventsSerializer


class TeamList(ListAPIView):
    """
    API endpoint that allows Teams to be viewed.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(RetrieveAPIView):
    """
    API endpoint that view a Team details.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = "id"


class TeamDelete(DestroyAPIView):
    """
    API endpoint that Delete a Team.
    """

    serializer_class = TeamSerializer
    lookup_field = "id"

    def get_queryset(self):
        return Team.objects.filter(id=self.kwargs['id'])


class TeamCreate(CreateAPIView):
    """
    API endpoint that Create a Team.
    """
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializer
    lookup_field = "id"


class TeamUpdate(RetrieveUpdateAPIView):
    """
    API endpoint that Update a Team information.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamEvents(RetrieveUpdateAPIView):
    """
    API endpoint that show Events of a team.
    """
    queryset = Event.objects.all()
    serializer_class = TeamEventsSerializer
    # lookup_field = "id"

    def get_queryset(self):
        return Event.objects.all()
