from rest_framework import serializers

from api.common import *

from ops.models import Person, CalendarEvent


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        exclude = ()


class CalendarEventSerializer(serializers.ModelSerializer):
    start_time = UnixEpochDateField()
    end_time = UnixEpochDateField()

    class Meta:
        model = CalendarEvent
        exclude = ()

    def is_valid_times(self):
        """
            Checks if times exact start of hour

            NOTE: It's sensitivity doesn't cover seconds

            @returns Boolean: Stating whether times are valid
        """
        if self.validated_data['start_time'].minute != 0 or self.validated_data['end_time'].minute != 0:
            return False
        return True