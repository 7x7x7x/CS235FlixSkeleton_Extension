from datetime import datetime

from domainmodel.movie import Movie


class Review:
    def __init__(self, movie: Movie, review_text: str, rating: int):
        if type(movie) is Movie:
            self.__movie = movie
        else:
            self.__movie = None

        if type(review_text) is str:
            self.__review_text = review_text.strip()
        else:
            self.__review_text = ""

        if 11 > rating > 0 and type(rating) is int:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp = datetime.now()

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f"<Review {self.__movie} Rating: {self.__rating}>"

    def __eq__(self, other):
        if self.__movie == other.movie and self.__rating == other.rating and self.__review_text == other.review_text and self.__timestamp == other.timestamp:
            return True
        else:
            return False


movie = Movie("Moana", 2016)
review_text = "This movie was very enjoyable."
rating = 8
review = Review(movie, review_text, rating)
review2 = Review(movie, review_text, 7)

print(review.movie)
print("Review: {}".format(review.review_text))
print("Rating: {}".format(review.rating))

if review == review2:
    print("SAME REVIEW")
else:
    print("NOT SAME")