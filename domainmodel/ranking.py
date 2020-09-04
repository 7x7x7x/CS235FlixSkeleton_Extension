from domainmodel.watchlist import WatchList
from domainmodel.movie import Movie

"""
Gets input from watchlist and 
"""


class Ranking:
    def __init__(self, watchlist_list=None):
        self.__ranking = dict()

        if isinstance(watchlist_list, list):
            for sub_watchlist in watchlist_list:
                for movie in sub_watchlist.watch_list:
                    try:
                        self.__ranking[movie.__repr__()] += 1
                    except:
                        self.__ranking[movie.__repr__()] = 1

    @property
    def ranking(self):
        return self.__ranking

    def import_watch_list(self, watch_list_in: WatchList):
        for movie in watch_list_in.watch_list:
            try:
                self.__ranking[movie.__repr__()] += 1
            except:
                self.__ranking[movie.__repr__()] = 1

    def import_multi_watch_list(self, watchlist_list=None):
        if isinstance(watchlist_list, list):
            for sub_watchlist in watchlist_list:
                for movie in sub_watchlist.watch_list:
                    try:
                        self.__ranking[movie.__repr__()] += 1
                    except:
                        self.__ranking[movie.__repr__()] = 1

    def most_watched(self, rows=10):
        sorted_ranking = sorted(self.__ranking.items(), key=lambda x: x[1], reverse=True)

        r_list = []
        x = 0
        for mv in sorted_ranking:
            if x < rows:
                # print(mv[0], mv[1])
                r_list.append(f"{x}: {mv[0]} Count {mv[1]}")
            else:
                return r_list

            x += 1

        return r_list


class TestRankingMethods:

    def test_init(self):
        wl1 = WatchList()
        wl2 = WatchList()
        wl3 = WatchList()
        wl4 = WatchList()
        wl5 = WatchList()
        wl6 = WatchList()

        wl1.add_movie(Movie("Movie a", 2016))
        wl1.add_movie(Movie("Movie b", 2011))
        wl1.add_movie(Movie("Movie c", 2013))
        wl1.add_movie(Movie("Movie d", 2013))
        wl1.add_movie(Movie("Movie e", 2015))

        wl2.add_movie(Movie("Movie b", 2011))
        wl2.add_movie(Movie("Movie c", 2013))
        wl2.add_movie(Movie("Movie e", 2015))

        wl3.add_movie(Movie("Movie a", 2016))
        wl3.add_movie(Movie("Movie e", 2015))

        wl4.add_movie(Movie("Movie b", 2011))
        wl4.add_movie(Movie("Movie d", 2013))
        wl4.add_movie(Movie("Movie e", 2015))

        wl5.add_movie(Movie("Movie a", 2016))
        wl5.add_movie(Movie("Movie b", 2011))
        wl5.add_movie(Movie("Movie c", 2013))

        wl6.add_movie(Movie("Movie a", 2016))
        wl6.add_movie(Movie("Movie b", 2011))
        wl6.add_movie(Movie("Movie e", 2015))

        wlc = [wl1, wl2, wl3, wl4, wl5, wl6]
        rank = Ranking(wlc)
        
        rank_dict = rank.ranking
        
        assert rank_dict["<Movie Movie a, 2016>"] == 4
        assert rank_dict["<Movie Movie b, 2011>"] == 5
        assert rank_dict["<Movie Movie c, 2013>"] == 3
        assert rank_dict["<Movie Movie d, 2013>"] == 2
        assert rank_dict["<Movie Movie e, 2015>"] == 5

    def test_import_watchlist(self):
        rank = Ranking()

        wl7 = WatchList()
        wl7.add_movie(Movie("Movie e", 2015))

        rank.import_watch_list(wl7)

        rank_dict = rank.ranking

        assert rank_dict["<Movie Movie e, 2015>"] == 1

    def test_importing_multiple(self):
        wl1 = WatchList()
        wl2 = WatchList()
        wl3 = WatchList()
        wl4 = WatchList()
        wl5 = WatchList()
        wl6 = WatchList()

        wl1.add_movie(Movie("Movie a", 2016))
        wl1.add_movie(Movie("Movie b", 2011))
        wl1.add_movie(Movie("Movie c", 2013))
        wl1.add_movie(Movie("Movie d", 2013))
        wl1.add_movie(Movie("Movie e", 2015))

        wl2.add_movie(Movie("Movie b", 2011))
        wl2.add_movie(Movie("Movie c", 2013))
        wl2.add_movie(Movie("Movie e", 2015))

        wl3.add_movie(Movie("Movie a", 2016))
        wl3.add_movie(Movie("Movie e", 2015))

        wl4.add_movie(Movie("Movie b", 2011))
        wl4.add_movie(Movie("Movie d", 2013))
        wl4.add_movie(Movie("Movie e", 2015))

        wl5.add_movie(Movie("Movie a", 2016))
        wl5.add_movie(Movie("Movie b", 2011))
        wl5.add_movie(Movie("Movie c", 2013))

        wl6.add_movie(Movie("Movie a", 2016))
        wl6.add_movie(Movie("Movie b", 2011))
        wl6.add_movie(Movie("Movie e", 2015))

        wlc = [wl1, wl2, wl3, wl4, wl5, wl6]
        rank = Ranking()
        rank.import_multi_watch_list(wlc)

        rank_dict = rank.ranking

        assert rank_dict["<Movie Movie a, 2016>"] == 4
        assert rank_dict["<Movie Movie b, 2011>"] == 5
        assert rank_dict["<Movie Movie c, 2013>"] == 3
        assert rank_dict["<Movie Movie d, 2013>"] == 2
        assert rank_dict["<Movie Movie e, 2015>"] == 5

    def test_rank(self):
        wl1 = WatchList()
        wl2 = WatchList()
        wl3 = WatchList()
        wl4 = WatchList()
        wl5 = WatchList()
        wl6 = WatchList()

        wl1.add_movie(Movie("Movie a", 2016))
        wl1.add_movie(Movie("Movie b", 2011))
        wl1.add_movie(Movie("Movie c", 2013))
        wl1.add_movie(Movie("Movie d", 2013))
        wl1.add_movie(Movie("Movie e", 2015))

        wl2.add_movie(Movie("Movie b", 2011))
        wl2.add_movie(Movie("Movie c", 2013))
        wl2.add_movie(Movie("Movie e", 2015))

        wl3.add_movie(Movie("Movie a", 2016))
        wl3.add_movie(Movie("Movie e", 2015))

        wl4.add_movie(Movie("Movie b", 2011))
        wl4.add_movie(Movie("Movie d", 2013))
        wl4.add_movie(Movie("Movie e", 2015))

        wl5.add_movie(Movie("Movie a", 2016))
        wl5.add_movie(Movie("Movie b", 2011))
        wl5.add_movie(Movie("Movie c", 2013))

        wl6.add_movie(Movie("Movie a", 2016))
        wl6.add_movie(Movie("Movie b", 2011))
        wl6.add_movie(Movie("Movie e", 2015))

        wlc = [wl1, wl2, wl3, wl4, wl5, wl6]
        rank = Ranking(wlc)

        tt = rank.most_watched().copy()

        assert tt[0] == '0: <Movie Movie b, 2011> Count 5'


