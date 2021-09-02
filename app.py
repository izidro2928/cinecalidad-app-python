from flask import Flask, render_template, request
from config import DevelopmentConfig
from models import db, Movie

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)


@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 20
    movies = Movie.query.paginate(page=page, per_page=per_page)
    title = "Inicio"
    return render_template('home_page.html', movies=movies, page=page, title=title)


@app.route('/pelicula/<int:movie_id>/', methods=['POST', 'GET'])
def details(movie_id):
    movie = Movie.query.get(movie_id)
    title = "Detalles"

    return render_template('single_page.html', movie=movie, title=title)


@app.route('/genero/<genre_name>/')
def genres(genre_name):
    page = request.args.get('page', 1, type=int)
    per_page = 20
    title = "Genero"
    movies = Movie.query.filter_by(genre=genre_name).paginate(page=page, per_page=per_page)
    return render_template("genre_page.html", movies=movies, page=page, title=title, genre_name=genre_name)


@app.route('/buscar/', methods=['POST', 'GET'])
def search():
    if request.method == "GET":
        title_m = request.args.get('s')
        movies = Movie.query.filter(Movie.title.like(f"{title_m}%")).limit(20).all()
        title = "Busqueda"
        return render_template('search_page.html', movies=movies, title=title)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0")
