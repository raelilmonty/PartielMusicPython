"""CLI internal functions."""

from rich.console import Console
from rich.table import Table

from . import db


def top_artists(top=10, file=None):
    table = Table(title=f'Top {top} artists')

    table.add_column('Artist')
    table.add_column('Number of invoice lines', justify='right')
    table.add_column('Total', justify='right')

    for num, row in enumerate(db.get_top_artists(top)):
        table.add_row(
            f'{num+1}. {row["Name"]}',
            str(row['invoicelines']),
            str(row['total']),
        )

    console = Console(file=file)
    console.print(table)


def top_tracks(top=10, file=None):
    table = Table(title=f'Top {top} tracks')

    table.add_column('Track')
    table.add_column('Total', justify='right')

    for num, row in enumerate(db.get_top_tracks(top)):
        table.add_row(
            f'{num+1}. {row["Name"]}',
            str(row['total']),
        )

    console = Console(file=file)
    console.print(table)


def top_customers(top=10, file=None):
    table = Table(title=f'Top {top} customers')

    table.add_column('Name')
    table.add_column('Total', justify='right')

    for num, row in enumerate(db.get_top_customers(top)):
        table.add_row(
            f'{num+1}. {row["Name"]}',
            str(row['total']),
        )

    console = Console(file=file)
    console.print(table)


def search_artists(term, file=None):
    table = Table(title=f"Search results for '{term}'")

    table.add_column("Artist ID", justify="right")
    table.add_column("Name")

    results = db.get_artist_by_name(term)
    for artist in results:
        table.add_row(str(artist["ArtistId"]), artist["Name"])

    console = Console(file=file)
    console.print(table)
    return [artist["Name"] for artist in results]
