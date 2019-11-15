from ui.clients import Client
from business.services import Service
from framework.repos import Repo
from framework.validators import Validator

persons = Repo()
events = Repo()
validator = Validator()
service = Service(persons, events, validator)
client = Client(service)

client.run()