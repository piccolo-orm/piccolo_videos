from movies.tables import Movie, Director


async def generate_data():
    """
    Add some directors and movies to the database.
    """
    george_lucas = Director(name="George Lucas", net_worth=6400)
    await george_lucas.save()

    movie = Movie(name="Star Wars", rating=8.6, director=george_lucas)
    await movie.save()

    print("Added data")
