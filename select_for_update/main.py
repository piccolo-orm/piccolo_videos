import asyncio

from piccolo.table import Table
from piccolo.columns.column_types import Varchar, Integer
from piccolo.engine.postgres import PostgresEngine


DB = PostgresEngine(config={"database": "piccolo_select_for_update"})


class Concert(Table, db=DB):
    name = Varchar()
    tickets_available = Integer()


async def book_tickets(ticket_count: int):
    async with Concert._meta.db.transaction():
        concert = (
            await Concert.objects()
            .where(Concert.name == "Awesome Concert")
            .first()
            .lock_rows()
        )

        if concert.tickets_available >= ticket_count:
            await concert.update_self(
                {
                    Concert.tickets_available: Concert.tickets_available
                    - ticket_count
                }
            )
        else:
            print("Not enough tickets are available!")


async def setup_db():
    await Concert.create_table(if_not_exists=True)
    await Concert.delete(force=True)


async def main():
    await setup_db()

    concert = Concert(
        {Concert.name: "Awesome Concert", Concert.tickets_available: 100}
    )
    await concert.save()

    await asyncio.gather(*[book_tickets(20) for _ in range(10)])

    await concert.refresh()
    print(concert.tickets_available)


if __name__ == "__main__":
    asyncio.run(main())
