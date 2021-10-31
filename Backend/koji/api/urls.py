from .views.UserViews import UserList, UserDetail, UserDelete, UserCreate, UserUpdate
from .views.TeamViews import TeamList, TeamDetail, TeamDelete, TeamCreate, TeamDelete, TeamEvents
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('user/list/', UserList.as_view(), name="UserList"),
    path('user/<email>/detail/', UserDetail.as_view(), name="UserDetail"),
    path('user/<email>/update/', UserUpdate.as_view(), name="UserUpdate"),
    path('user/<email>/delete/', UserDelete.as_view(), name="UserDelete"),
    path('user/create/', UserCreate.as_view(), name="UserCreate"),
    path('team/list/', TeamList.as_view(), name="TeamList"),
    path('team/<id>/detail/', TeamDetail.as_view(), name="TeamDetail"),
    path('team/<id>/events/', TeamEvents.as_view(), name="TeamEvents"),
    path('team/<id>/delete/', TeamDelete.as_view(), name="TeamDelete"),
    path('team/create/', TeamCreate.as_view(), name="TeamCreate"),
]
