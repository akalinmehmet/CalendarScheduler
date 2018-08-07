import json

from django.http import JsonResponse
from django.db.models import Q

from rest_framework import viewsets, versioning, status as drf_status
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from api.common import *

from ops.models import CalendarEvent, Person
from ops.api.serializers import CalendarEventSerializer, PersonSerializer