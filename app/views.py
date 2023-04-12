"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import make_response, render_template, request, jsonify, send_file, send_from_directory
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
from .models import Movie
from .forms import MovieForm
import os


###
# Routing for your application.
###

@app.route("/api/v1/movies", methods=['POST', 'GET'])
def movies():
    form = MovieForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            poster = form.poster.data
            filename = secure_filename(poster.filename) 
            poster.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            movie = Movie(title, description, filename)
            db.session.add(movie)
            db.session.commit()
            response = {
                "message": "Movie Successfully added",
                "title": title,
                "poster": filename,
                "description": description
            }
            return jsonify(response), 200
        else:
            return jsonify({"errors":form_errors(form)}), 400
    if request.method == 'GET':
       return jsonify({"Movies":getMovies()}), 200


@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
  return jsonify({'csrf_token': generate_csrf()})
  


def getMovies():
    movies = db.session.execute(db.select(Movie)).scalars()
    movieslst=[]
    for movie in movies:
        output = {
            "id": movie.id,
            "title":movie.title,
            "description": movie.description,
            "poster": f"/api/v1/posters/{movie.poster}" 
        }
        movieslst.append(output)
    return movieslst

@app.route("/api/v1/posters/<filename>")
def getPoster(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)


@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404