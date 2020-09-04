from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    def __init__(self, user_name: str, password: str):
        self.__user_name = user_name.lower().strip()
        self.__password = password

        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def watch_movie(self, movie: Movie):
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review: Review):
        self.__reviews.append(review)

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if self.__user_name == other.user_name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.__user_name < other.user_name:
            return True
        else:
            return False

    def __hash__(self):
        return hash(self.__user_name)


user1 = User('Martin', 'pw12345')
user2 = User('Ian', 'pw67890')
user3 = User('Daniel', 'pw87465')
print(user1)
print(user2)
print(user3)