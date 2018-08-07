from common import *



class CalendarEventViewSet(viewsets.ModelViewSet):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer
    filter_fields = ('person', 'start_time', 'end_time')


    @list_route(url_path="search", methods=['GET'])
    @request_data_has(data_type="data", keys=["candidate_id"])
    def search(self, request):
        data = request.data

        # Fetch CalendarEvents of candidate with given ID
        student_availabilities = CalendarEvent.objects.filter(person__id=data["candidate_id"])
        interviewer_availabilities = []

        # For each candidate's availability fetch appropriate interviewer availability
        for student_ava in student_availabilities:
            possible_availabilities = CalendarEvent.objects.filter(Q(person__person_type=Person.INTERVIEWER) &
                                                                   ((Q(start_time__lte=student_ava.start_time) & Q(end_time__gte=student_ava.start_time)) |
                                                                    (Q(start_time__lte=student_ava.end_time) & Q(end_time__gte=student_ava.end_time))))

            if possible_availabilities:
                interviewer_availabilities.append([])

            for possible in possible_availabilities:
                # Append possible interviewer timeslots to response
                interviewer_availabilities[-1].append({'slots': possible.slots(start_time=student_ava.start_time, end_time=student_ava.end_time),
                                                       'interviewer': PersonSerializer(possible.person, many=False).data})

        return JsonResponse(interviewer_availabilities, safe=False, status=drf_status.HTTP_200_OK)


    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if times are 1 hour intervals
        if not serializer.is_valid_times():
            return Response({'error': "Calendar Events should be o'clocks"}, status=403)

        # Perform Create
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=drf_status.HTTP_201_CREATED)
