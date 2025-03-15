
fav_movies = ['The Holy Grail', 'The Life of Brian', 'Dune']

print(len(fav_movies))

fav_movies.append('The Dark Knight')

print(len(fav_movies))

print(fav_movies)

fav_movies.insert(1, 'The Empire Strikes Back')

fav_movies.insert(3, 'The Matrix')

print(fav_movies)

print(len(fav_movies))

del(fav_movies[2])

print(fav_movies)