from EventOrganiser.business.services import CommandsService, PersonService, EventService, AttendanceService
from EventOrganiser.framework.repos import CommandFileRepo, PersonFileRepo, EventFileRepo, AttendanceFileRepo
from EventOrganiser.ui.uis import ConsoleUI

commands = CommandFileRepo("commands.json", [])
persons = PersonFileRepo("persons.json", [])
events = EventFileRepo("events.json", [])
attendances = AttendanceFileRepo("attendances.json", [])

commands_service = CommandsService(commands)
persons_service = PersonService(persons)
events_service = EventService(events)
attendances_service = AttendanceService(attendances)

ui = ConsoleUI(commands_service, persons_service, events_service, attendances_service)

ui.run_application()
