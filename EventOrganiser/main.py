from EventOrganiser.business.services import CommandsService, PersonService, EventService, AttendanceService
from EventOrganiser.framework.repos import CommandFileRepo, PersonFileRepo, EventFileRepo, AttendanceFileRepo
from EventOrganiser.framework.validators import Validator
from EventOrganiser.ui.uis import ConsoleUI

validator = Validator()

commands = CommandFileRepo("commands.json")
persons = PersonFileRepo(validator, "persons.json", [])
events = EventFileRepo(validator, "events.json", [])
attendances = AttendanceFileRepo(validator, "attendances.json", [])

commands_service = CommandsService(commands)
persons_service = PersonService(persons)
events_service = EventService(events)
attendances_service = AttendanceService(persons.items, events.items, attendances)

ui = ConsoleUI(commands_service, persons_service, events_service, attendances_service)

ui.run_application()
