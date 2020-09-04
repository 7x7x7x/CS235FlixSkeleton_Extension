class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        self.__colleagues = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if self.__actor_full_name == other.actor_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__actor_full_name < other.actor_full_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if type(colleague) is Actor:
            self.__colleagues.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.__colleagues:
            return True
        else:
            return False


class TestActorMethods:

    def test_init(self):
        actor1 = Actor("Angelina Jolie")
        # print(actor1)
        actor2 = Actor("Kate N")
        # print(actor2)
        actor3 = Actor(42)
        # print(actor3)

        actor1.add_actor_colleague(actor2)

        assert actor1.check_if_this_actor_worked_with(actor2) is True
