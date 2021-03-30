from flask import flask

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/watch")
def watch():
    return render_template("movies.html",
                            movies=movies,
                            name="SRS")

if __name__ == "__main__":
    app.run()