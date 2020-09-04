class Genre:
    def __init__(self, g_name: str):
        if g_name == "" or type(g_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = g_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if self.__genre_name == other.genre_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__genre_name < other.genre_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__genre_name)

"""
genre1 = Genre("Horror")
print(genre1)
genre2 = Genre("")
print(genre2)
"""