from EventOrganiser.business.services import CommandsService, PersonService, EventService, AttendanceService
from EventOrganiser.framework.repos import CommandFileRepo, PersonFileRepo, EventFileRepo, AttendanceFileRepo
from EventOrganiser.framework.validators import Validator
from EventOrganiser.ui.uis import ConsoleUI


commands = CommandFileRepo("commands.json")
persons = PersonFileRepo("persons.json", [])
events = EventFileRepo("events.json", [])
attendances = AttendanceFileRepo("attendances.json", [])

validator = Validator()

commands_service = CommandsService(commands)
persons_service = PersonService(validator, persons)
events_service = EventService(validator, events)
attendances_service = AttendanceService(validator, attendances)

ui = ConsoleUI(commands_service, persons_service, events_service, attendances_service)

ui.run_application()
