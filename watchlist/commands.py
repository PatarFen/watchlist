import click

from watchlist import app, db
from watchlist.models import Movie

@app.cli.command()
#@click.option('--drop', is_flag=True, help='Create after drop.')
def drop():
    """Drop all data."""
    db.drop_all()
    click.echo('Database clean.')

@app.cli.command()
def forge():

    db.create_all()

    
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    for _ in movies:
        movie = Movie(title = _['title'], year = _['year'])
        db.session.add(movie)
    
    db.session.commit()
    click.echo("Generated Fake data~")