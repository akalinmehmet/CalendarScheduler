from django.conf.urls import url, include
from rest_framework import routers

urlpatterns = [
    url(r'^ops/', include('ops.api.urls')),
]