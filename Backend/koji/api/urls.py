from .views import UserList
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('users/', UserList.as_view(), name="UserList"),
]
