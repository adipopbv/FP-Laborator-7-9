class Tests:

    class ServiceTest:
        from business.services import Service
        from domain.entities import Id, Name, CityName, StreetName, Number, Adress, Person
        from framework.validators import Validator
        from framework.repos import Repo

        def run_all(self):
            self.create_adress_test()
            self.creare_person_test()
            self.add_person_to_repo_test()

        def create_adress_test(self):
            persons = self.Repo()
            events = self.Repo()
            validator = self.Validator()
            service = self.Service(persons, events, validator)
            adress = service.create_adress("cluj", "dorobantilor", "123")
            assert adress.get_city_name().get_value() == "cluj"
            assert adress.get_street_name().get_value() == "dorobantilor"
            assert adress.get_number().get_value() == "123"

        def creare_person_test(self):
            persons = self.Repo()
            events = self.Repo()
            validator = self.Validator()
            service = self.Service(persons, events, validator)
            adress = service.create_adress("cluj", "dorobantilor", "123")
            person = service.create_person("1", "cineva", adress)
            assert person.get_id().get_value() == "1"
            assert person.get_name().get_value() == "cineva"
            assert person.get_adress().get_city_name().get_value() == "cluj"
            assert person.get_adress().get_street_name().get_value() == "dorobantilor"
            assert person.get_adress().get_number().get_value() == "123"

        def add_person_to_repo_test(self):
            persons = self.Repo()
            events = self.Repo()
            validator = self.Validator()
            service = self.Service(persons, events, validator)
            service.add_person_to_repo(persons, "1", "cineva", "cluj", "dorobantilor", "123")
            assert service.get_persons().count() == 1
            assert not service.get_persons().count() == 0

    class CommandsRepoTest:
        from framework.repos import CommandsRepo
        from domain.entities import Command

        def run_all(self):
            self.get_commands_with_id_test()

        def get_commands_with_id_test(self):
            command1 = self.Command("1", None)
            command2 = self.Command("2", None)
            commandsRepo = self.CommandsRepo(command1, command2)
            assert commandsRepo.get_command_with_id("2") == command2
            assert not commandsRepo.get_command_with_id("2") == command1
            try:
                assert commandsRepo.get_command_with_id(1)
                assert False
            except:
                assert True

    class RepoTest:
        from framework.repos import Repo

        def run_all(self):
            self.add_test()
            self.count_test()

        def add_test(self):
            repo = self.Repo(1, 2, 3)
            repo.add(4)
            assert repo.get_items() == [1,2,3,4]
            assert not repo.get_items() == [1,2,3]

        def count_test(self):
            repo = self.Repo(1, 2, 3)
            assert repo.count() == 3
            assert not repo.count() == 0

    class ValidatorTest:
        from framework.validators import Validator
        from domain.entities import Id, Name, CityName, StreetName, Number, Adress, Person

        def run_all(self):
            self.validate_person_test()

        def validate_person_test(self):
            validator = self.Validator()
            person = self.Person(self.Id("123"), self.Name("kajner"), self.Adress(self.CityName("hkuygdkf"), self.StreetName("knwjv"), self.Number("51")))
            try:
                validator.validate_person(person)
                assert True
            except:
                assert False
            person = self.Person(self.Id(123), self.Name("kajner"), self.Adress(self.CityName("hkuygdkf"), self.StreetName(2314), self.Number(1)))
            try:
                validator.validate_person(person)
                assert False
            except:
                assert True

    #------------------

    def __init__(self):
        self._service_test = self.ServiceTest()
        self._repo_test = self.RepoTest()
        self._commands_repo_test = self.CommandsRepoTest()
        self._validator_test = self.ValidatorTest()

    def get_service_test(self):
        return self._service_test

    def get_repo_test(self):
        return self._repo_test

    def get_commands_repo_test(self):
        return self._commands_repo_test

    def get_validator_test(self):
        return self._validator_test

    #------------------

    def run_all(self):
        self.get_validator_test().run_all()
        self.get_repo_test().run_all()
        self.get_commands_repo_test().run_all()
        self.get_service_test().run_all()
