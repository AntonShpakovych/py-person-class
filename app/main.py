class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person(human["name"], human["age"])

    for human in people:
        if human.get("wife"):
            wife = Person.people[human["wife"]]
            Person.people[human["name"]].wife = wife
        elif human.get("husband"):
            husband = Person.people[human["husband"]]
            Person.people[human["name"]].husband = husband
    return [instance for instance in Person.people.values()]
