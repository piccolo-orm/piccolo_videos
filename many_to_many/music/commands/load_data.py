from music.tables import Band, Genre, GenreToBand

def load_data():
    Band.insert(
        Band(name="Pythonistas"),
        Band(name="Rustaceans"),
        Band(name="C-Sharps"),
    ).run_sync()

    Genre.insert(
        Genre(name="Rock"),
        Genre(name="Folk"),
        Genre(name="Classical"),
    ).run_sync()

    GenreToBand.insert(
        GenreToBand(band=1, genre=1),
        GenreToBand(band=1, genre=2),
        GenreToBand(band=2, genre=2),
        GenreToBand(band=3, genre=1),
        GenreToBand(band=3, genre=3),
    ).run_sync()
