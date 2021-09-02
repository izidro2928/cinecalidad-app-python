from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(250), nullable=True)
    poster = db.Column(db.Text, nullable=True)
    overview = db.Column(db.Text, nullable=True)
    imdb = db.Column(db.VARCHAR(250), nullable=True)
    genre = db.Column(db.VARCHAR(250), nullable=True)
    video1 = db.Column(db.Text, nullable=True)
    video2 = db.Column(db.Text, nullable=True)
    video3 = db.Column(db.Text, nullable=True)
    video4 = db.Column(db.Text, nullable=True)
    video5 = db.Column(db.Text, nullable=True)
    video6 = db.Column(db.Text, nullable=True)
    video7 = db.Column(db.Text, nullable=True)
    trailer = db.Column(db.Text, nullable=True)
