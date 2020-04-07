from django.conf.urls import url

from .views import *


urlpatterns = [
  url(r'^users/$', UserList.as_view()),
]