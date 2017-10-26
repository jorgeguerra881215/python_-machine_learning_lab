import pandas as pd

def get_movie_data():
    users_names = ['user_id', 'gender', 'age', 'occupation', 'zip']
    users = pd.read_table('../data/ml-1m/users.dat', sep='::', header=None, names=users_names )

    movies_names = ['movie_id', 'title', 'genres']
    movies = pd.read_table('../data/ml-1m/movies.dat', sep='::', header=None, names=movies_names)

    rating_names = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_table('../data/ml-1m/ratings.dat', sep='::', header=None, names=rating_names)

    data = pd.merge(pd.merge(ratings, users), movies)
    print data


if __name__ == "__main__":
    get_movie_data()
    print 'finish'