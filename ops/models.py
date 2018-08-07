# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from datetime import datetime, timedelta

from django.db import models


class Person(models.Model):
    CANDIDATE, INTERVIEWER = "1", "2"
    PERSON_TYPES = (
        (CANDIDATE, "Candidate"),
        (INTERVIEWER, "Interviewer")
    )

    username = models.CharField("Username", max_length=50, default=uuid.uuid4(), 
                                blank=False, null=False)
    person_type = models.CharField("Person Type", max_length=1, default="1", 
                                   choices=PERSON_TYPES, blank=False, null=False)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return "{username}".format(username=self.username)


class CalendarEvent(models.Model):
    person = models.ForeignKey(Person, blank=False, null=False)
    start_time = models.DateTimeField(verbose_name="Start Time", blank=False, null=False)
    end_time = models.DateTimeField(verbose_name="End Time", blank=False, null=False)

    class Meta:
        verbose_name = 'Calender Event'
        verbose_name_plural = 'Calender Events'

    def __str__(self):
        return "{username}:  {start} - {end}".format(username=self.person.username, 
                                                     start=self.start_time, end=self.end_time)

    def slots(self, start_time, end_time):
        """
            Returns 1-hour time intervals within start time and end times

            :param start_time:  Start time of the interval to be searched
            :param end_time:    End time of the interval to be searched
            @returns List:   List of available time slots
        """
        slots = []
        temp_start_time = max(self.start_time, start_time) 
        temp_end_time = min(self.end_time, end_time)
        while temp_start_time < temp_end_time:
            slots.append((temp_start_time.isoformat(), (temp_start_time + timedelta(hours=1)).isoformat() ))
            temp_start_time += timedelta(hours=1)

        return slots