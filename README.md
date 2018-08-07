# CalendarScheduler

## Summary

This project aims to match candidate and interviewer availabilities by 1-hour slots.

## Installation

Create a virtual environment (if you are using virtualenv, use the following)

```
virtualenv chemondis
cd chemondis
source bin/activate
```

Clone the repository and install requirements

```
git clone https://github.com/akalinmehmet/CalendarScheduler.git
cd CalendarScheduler
pip install -r requirements.txt
```

Run the server and enjoy the basic API

```
python manage.py runserver
```

## API

### Candidate/Interviewer

Person model has a field of `person_type` which denotes the person whether s/he is a candidate or an interviewer.

| Person Type | Identifier | 
|-------------| -----------| 
| Candidate   | 1          |
| Interviewer | 2          |

### Create Candidate/Interviewer

Following API Call is going to create a candidate with username 'mehmet'

```
http POST <base_api>/api/ops/persons/ username=mehmet person_type=1
```

Similarly, following API Call is going to create an interviewer with username `marina`

```
http POST <base_api>/api/ops/persons/ username=marina person_type=2
```

### Fetch Candidates/Interviewers

Following API Call is going to get a list of all candidates

```
http GET <base_api>/api/ops/persons/ 
```

And it will return a response like in the following format

```
[
    {
        'id': 1,
        'username': 'mehmet',
        'person_type': '1'
    },
    {
        'id': 2,
        'username': 'marina',
        'person_type': '2'
    },
]

```


### Fetch Single Candidate/Interviewer

Following API Call is used to retreive information of a single candidate

```
http GET <base_api>/api/ops/persons/2/ 
```

And it will return a response like in the following format

```
{
    'id': 2,
    'username': 'marina',
    'person_type': '2'
}

```


### Calendar Event

Calendar Events are the models to store availabilities of both candidates and interviewers.


### Create a Calendar Event

Following API Call is going to create a calendar event for the interviewer `marina` for the interview between 7 August 2018 10:00 to 7 August 2018 18:00 in both UTC

```
http POST <base_api>/api/ops/calendarevents/ person=2 start_time=1533636000 end_time=1533664800
```

And similarly following API Call is going to create a calendar event for the candidate `mehmet` for the interview between 7 August 2018 13:00 to 7 August 2018 15:00 in both UTC

```
http POST <base_api>/api/ops/calendarevents/ person=1 start_time=1533646800 end_time=1533654000
```


### Fetch Calendar Events

Following API Call is going to fetch all calendar events 

```
http GET <base_api>/api/ops/calendarevents/ 
```

It will return a response like in following format

```
[
    {
        "end_time": 1533664800, 
        "id": 1, 
        "person": 2, 
        "start_time": 1533636000
    }, 
    {
        "end_time": 1533654000, 
        "id": 2, 
        "person": 1, 
        "start_time": 1533646800
    },
]
```

### Retrieve a Single Calendar Event

Following API Call is going to retrive a calendar event

```
http GET <base_api>/api/ops/calendarevents/1/
```

It will return a response like in following format

```
{
    "end_time": 1533664800, 
    "id": 1, 
    "person": 2, 
    "start_time": 1533636000
}
```

### Search for available interviewers for a candidate

Following API Call is going to search for possible interviewers for a given candidate

```
http GET <base_api>/api/ops/calendarevents/search/ candidate_id=1
```

It will return a response like in the following format. It shows different time slots for an interviewers

```
[
    [
        {
            "interviewer": {
                "id": 7, 
                "person_type": "2", 
                "username": "marina"
            }, 
            "slots": [
                [
                    "2018-08-07T13:00:00+00:00", 
                    "2018-08-07T14:00:00+00:00"
                ], 
                [
                    "2018-08-07T14:00:00+00:00", 
                    "2018-08-07T15:00:00+00:00"
                ]
            ]
        }
    ]
]
```