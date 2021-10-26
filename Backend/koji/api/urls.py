from .views.UserViews import UserList, UserDetail, UserDelete,UserCreate,UserUpdate
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('user/list/', UserList.as_view(), name="UserList"),
    path('user/<email>/detail/', UserDetail.as_view(), name="UserDetail"),
    path('user/<email>/update/', UserUpdate.as_view(), name="UserUpdate"),
    path('user/<email>/delete/', UserDelete.as_view(), name="UserDelete"),
    path('user/create/', UserCreate.as_view(), name="UserCreate"),
]
