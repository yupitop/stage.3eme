from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///manga.db"
db = SQLAlchemy(app)

class Manga(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(100), nullable=False)

@app.before_request
def create_db():
    db.create_all()

@app.route("/manga/<int:id>", methods=["GET"])
def get_manga(id):
    manga = Manga.query.get(id)
    if manga is None:
        return jsonify({"error": "Manga not found"}), 404
    return jsonify({
        "title": manga.title,
        "author": manga.author,
        "summary": manga.summary,
        "ranking": manga.ranking,
        "image": manga.image
    })

if __name__ == "__main__":
    app.run(debug=True)
    print("")