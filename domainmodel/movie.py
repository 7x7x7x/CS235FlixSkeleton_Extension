from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:
    def __init__(self, title: str, year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

        if type(year) is not int or year < 1900:
            self.__year = None
        else:
            self.__year = year

        self.__description = ""
        self.__director = None
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = 0

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title: str):
        if new_title == "" or type(new_title) is not str:
            pass
        else:
            self.__title = new_title.strip()

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year < 1900:
            pass
            # raise ValueError("Year cannot be below 1900")
        else:
            self.__year = new_year

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, new_director):
        self.__director = new_director

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if runtime < 1:
            raise ValueError("Runtime must be positive")
        else:
            self.__runtime_minutes = runtime

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actors_list):
        if type(actors_list) is list:
            self.__actors = actors_list

    def add_actor(self, new_actor: Actor):
        if type(new_actor) is Actor:
            self.__actors.append(actor)

    def remove_actor(self, del_actor: Actor):
        try:
            index = self.__actors.index(del_actor)
        except ValueError:
            pass
        else:
            self.__actors.pop(index)

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres_list):
        if type(genres_list) is list:
            self.__genres = genres_list

    def add_genre(self, genre: Genre):
        if type(genre) is Genre:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        try:
            index = self.__genres.index(genre)
        except ValueError:
            pass
        else:
            self.__genres.pop(index)

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, desc: str):
        if type(desc) is str:
            self.__description = desc.strip()

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__year}>"

    def __eq__(self, other):
        if self.__title == other.title and self.__year == other.year:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__title == other.title:
            if self.__year < other.year:
                return True
            else:
                return False
        elif self.__title < other.title:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__title + str(self.__year))


"""
movie = Movie("Moana", 2016)
print(movie)

director = Director("Ron Clements")
movie.director = director
print(movie.director)

actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
for actor in actors:
    movie.add_actor(actor)
print(movie.actors)

movie.runtime_minutes = 107
print("Movie runtime: {} minutes".format(movie.runtime_minutes))
movie.runtime_minutes = 11

g = Genre("Horror")
g2 = Genre("Romance")
movie.add_genre(g)
movie.add_genre(g2)

movie.remove_genre(g2)
movie.remove_genre(g2)
print(movie.genres)

g3 = Genre("Action")

g_list = [g, g2, g3]

movie.genres = g_list
print(movie.genres)

movie.description = "    lol     "
print(movie.description)
movie.description = ""
print(movie.description)

movie2 = Movie("Moana", 2017)

if movie > movie2:
    print("movie > movie2")
else:
    print("movie !> movie2")

print(hash(movie))
print(hash(movie2))
"""