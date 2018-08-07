import pytz
from datetime import datetime
from functools import wraps

from django.http import JsonResponse

from rest_framework import serializers



class UnixEpochDateField(serializers.DateTimeField):
    def to_representation(self, value):
        """ Return epoch time for a datetime object or ``None``"""
        import calendar

        try:
            return int(calendar.timegm(value.timetuple()))
        except (AttributeError, TypeError):
            return None

    def to_internal_value(self, value):
        return datetime.fromtimestamp(int(value), pytz.utc)


def request_data_has(data_type, keys=[]):
    """
        Ensure that request exists and has the parameters defined in keys list(for viewset method)
    """
    def decorator(method):
        @wraps(method)
        def wrapper(self, request, *args, **kwargs):
            data = eval('request.' + data_type)
            errors = {}
            for k in keys:
                if k not in data or data[k] == None:
                    error = "This parameter is required"
                    errors[k] = error
            if errors:
                return JsonResponse(errors, status=400)
            return method(self, request, *args, **kwargs)
        return wrapper
    return decorator
