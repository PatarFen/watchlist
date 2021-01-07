from flask import render_template, request, url_for, redirect, flash

from watchlist import app, db
from watchlist.models import Movie, Comment

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':

        #This part is about add new movie
        title = request.form.get('title')
        year = request.form.get('year')
        
        if title and year:
            if not title or not year or len(year) > 4 or len(title) > 60:
                flash('Invalid input.')
                return redirect(url_for('index'))
            
            movie = Movie(title = title, year = year)
            db.session.add(movie)
            db.session.commit()
            flash("Item Created")

        #THis part is about add new comment
        name = request.form.get('name')
        content = request.form.get('content')
        
        if name and content:
            if not name or not content:
                flash('Invalid input.')
                return redirect(url_for('index'))
            
            comment = Comment(name = name, content =content)
            db.session.add(comment)
            db.session.commit()
            flash('Comment added')
        
        return redirect(url_for('index'))

    movies = Movie.query.all()
    comments = Comment.query.all()
    return render_template('index.html', movies=movies, comments = comments, name = "Peter")

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