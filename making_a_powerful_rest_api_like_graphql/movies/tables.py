from piccolo.columns import (
    ForeignKey,
    Integer,
    Real,
    Varchar,
)
from piccolo.table import Table


class Director(Table):
    name = Varchar(length=300, null=False)
    net_worth = Integer(secret=True, help_text="In millions")


class Movie(Table):
    name = Varchar(length=300)
    rating = Real(help_text="The rating on IMDB.")
    director = ForeignKey(references=Director)
