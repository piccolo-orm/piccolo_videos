from piccolo.columns.column_types import (
    ForeignKey,
    LazyTableReference,
    Varchar
)
from piccolo.columns.readable import Readable
from piccolo.columns.m2m import M2M
from piccolo.table import Table


class Band(Table):
    name = Varchar()
    genres = M2M(LazyTableReference("GenreToBand", module_path=__name__))

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(template="%s", columns=[cls.name])


class Genre(Table):
    name = Varchar()
    bands = M2M(LazyTableReference("GenreToBand", module_path=__name__))

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(template="%s", columns=[cls.name])


# This is our joining table:
class GenreToBand(Table):
    band = ForeignKey(Band)
    genre = ForeignKey(Genre)

    @classmethod
    def get_readable(cls) -> Readable:
        return Readable(
            template="%s - %s",
            columns=[cls.band.name, cls.genre.name]
        )
