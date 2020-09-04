import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                self.__dataset_of_movies.append(Movie(title, release_year))
                print(f"Movie {index} with title: {title}, release year {release_year}")

                actors = row['Actors'].split(',')
                temp_director = Director(row['Director'])
                genres = row['Genre'].split(',')

                for a in actors:
                    temp_actor = Actor(a.strip())
                    if temp_actor not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(temp_actor)

                if temp_director not in self.__dataset_of_directors:
                    self.__dataset_of_directors.append(temp_director)

                for g in genres:
                    temp_genre = Genre(g.strip())
                    if temp_genre not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(temp_genre)

                index += 1

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors



"""
mv_reader = MovieFileCSVReader("K:/PycharmProjects/CS235FlixSkeleton/datafiles/Data1000Movies.csv")
mv_reader.read_csv_file()

print(f'number of unique movies: {len(mv_reader.dataset_of_movies)}')
print(f'number of unique actors: {len(mv_reader.dataset_of_actors)}')
print(f'number of unique directors: {len(mv_reader.dataset_of_directors)}')
print(f'number of unique genres: {len(mv_reader.dataset_of_genres)}')
"""