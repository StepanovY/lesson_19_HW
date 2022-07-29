from dao.model.movie import Movie


class MovieDAO:
    """
    Класс с методами доступа к данным
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        Метод получения одного Movie
        """
        return self.session.query(Movie).get(bid)

    def get_all(self):
        """
        Метод получения одного всех Movies
        """
        # А еще можно сделать так, вместо всех методов get_by_*
        # t = self.session.query(Movie)
        # if "director_id" in filters:
        #     t = t.filter(Movie.director_id == filters.get("director_id"))
        # if "genre_id" in filters:
        #     t = t.filter(Movie.genre_id == filters.get("genre_id"))
        # if "year" in filters:
        #     t = t.filter(Movie.year == filters.get("year"))
        # return t.all()
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        """
        Метод получения Movies с фильтрацией по параметру
        :param val: director_id
        :return:
        """
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        """
        Метод получения Movies с фильтрацией по параметру
        :param val: genre_id
        :return:
        """
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        """
        Метод получения Movies с фильтрацией по параметру
        :param val: year
        :return:
        """
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_d):
        """
        Метод создания Movie
        """
        ent = Movie(**movie_d)

        self.session.add(ent)
        self.session.commit()

        return ent

    def delete(self, rid):
        """
        Метод удаления Movie
        """
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        """
        Метод обновления Movie
        """
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie_d.get("title")
        movie.description = movie_d.get("description")
        movie.trailer = movie_d.get("trailer")
        movie.year = movie_d.get("year")
        movie.rating = movie_d.get("rating")
        movie.genre_id = movie_d.get("genre_id")
        movie.director_id = movie_d.get("director_id")

        self.session.add(movie)
        self.session.commit()
