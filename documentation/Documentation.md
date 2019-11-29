# Event Organiser

## Statement:

Scrieți o aplicație pentru organizarea de evenimente.
Aplicația stochează persoane și evenimente.

## Functionalities list:

1. Modifications:
    1. Add persons
    2. Add events
    3. Modify persons
    4. Modify events
2. Searches:
    1. Search persons
    2. Search events
3. Enrolling persons to events
4. Reports:
    1. Events which a person will attend, ordered alphabeticaly by description, date
    2. Persons attending the most events
    3. The first 20% events with the most attendees (description, attendees count)

## Iteration plan:

### Iteration 1:

- Base app
- 1.1

### Iteration 2:

- 1.2
- 1.3
- 1.4
- 2.1
- 2.2

### Iteration 3:

- 3
- 4.1
- 4.2
- 4.3

## Run scenarios:

| User input | App output | Description of action|
| --- | --- | --- |
| 0 | Exit application | Application stops running |
| 1 | Add person | Application gets input for person's data and adds it to the repo |
| 2 | Add event | Application gets input for event's data and adds it to the repo |
| 3 | Modify person | Application gets the first person to be modified by given field and the modified data and modifies the corresponding person |
| 4 | Modify event | Application gets the first event to be modified by given field and the modified data and modifies the corresponding event |
| 5 | Search person | Application displays the persons by the given field and displays their data |
| 6 | Search event | Application displays the events by the given field and displays their data |
| 7 | Enroll person | App enrolls a person to an event by id |
| 8 | Ordered events attended by person | App gets all events attended by person ordered by description, date |
| 9 | Persons attending most events | App gets the persons attending the most events |
| 10 | First 20% events with most attendees | Gets the first 20% events with the most attendees |
| 11 | Generate random events | Generates randomly a given numner of events and adds them to the repo |
| 12 | Persons attending fewest events | Gets the persons attending the fewest events ordered by name |