from flask import render_template, request, url_for, redirect, flash

from watchlist import app, db
from watchlist.models import Movie

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form.get('title')
        year = request.form.get('year')

        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('index'))
        
        movie = Movie(title = title, year = year)
        db.session.add(movie)
        db.session.commit()
        flash("Item Created")
        
        return redirect(url_for('index'))

    movies = Movie.query.all()
    return render_template('index.html', movies=movies, name = "Peter")

@app.route('/movie/edit/<int:movie_id>', methods = ['GET', 'POST'])
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)

    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']

        if not title or not year or len(year) > 4 or len(title) > 60:
            flash('Invalid input.')
            return redirect(url_for('edit', movie_id=movie_id))

        movie.title = title
        movie.year = year
        db.session.commit()
        flash('Item updated')
        return redirect(url_for('index'))

    return render_template('edit.html', movie = movie)

@app.route('/movie/delete/<int:movie_id>', methods = ['POST'])
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash("item deleted!")
    
    return redirect(url_for('index'))