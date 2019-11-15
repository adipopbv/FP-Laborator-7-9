from ui.clients import Client
from business.services import Service
from framework.repos import Repo

persons = Repo()
events = Repo()
service = Service(persons, events)
client = Client(service)

client.run()