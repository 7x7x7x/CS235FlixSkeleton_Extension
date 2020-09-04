from domainmodel.movie import Movie

class WatchList:
    def __init__(self):
        self.__watch_list = []

    @property
    def watch_list(self):
        return self.__watch_list

    def add_movie(self, movie: Movie):
        if movie not in self.__watch_list:
            self.__watch_list.append(movie)

    def remove_movie(self, movie: Movie):
        try:
            index = self.__watch_list.index(movie)
        except ValueError:
            pass
        else:
            self.__watch_list.pop(index)

    def select_movie_to_watch(self, index):
        if index >= len(self.__watch_list):
            # print("NONE RETURN")
            return None
        else:
            # print("RETURN MOVIE")
            return self.__watch_list[index]

    def size(self):
        return len(self.__watch_list)

    def first_movie_in_watchlist(self):
        return self.select_movie_to_watch(0)

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.size():
            result = self.select_movie_to_watch(self.n)
            self.n += 1
            return result
        else:
            raise StopIteration