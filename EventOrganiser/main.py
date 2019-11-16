from ui.clients import Client
from business.services import Service
from framework.repos import IdRepo, IdFileRepo
from framework.validators import Validator
from tests import Tests

tests = Tests()
persons = IdFileRepo("persons.json")
#events = Repo()
events = IdFileRepo("events.json")
validator = Validator()
service = Service(persons, events, validator)
client = Client(service)

tests.run_all()
client.run()