from rest_framework import routers

from django.conf.urls import url, include

import views


router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'calendarevents', views.CalendarEventViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
