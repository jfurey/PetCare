from flask import Blueprint, jsonify, request, current_app
import MySQLdb.cursors

bp = Blueprint("resources", __name__, url_prefix="/resources")


@bp.get("", strict_slashes=False)
def get_resources():
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM resources")
    results = cursor.fetchall()
    return jsonify(results)


@bp.post("", strict_slashes=False)
def add_resource():
    data = request.get_json()

    title = data.get("title")
    url = data.get("url")
    category = data.get("category")

    if not title or not url:
        return jsonify({"error": "Missing required fields"}), 400

    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute("""
        INSERT INTO resources (title, url, category)
        VALUES (%s, %s, %s)
    """, (title, url, category))
    current_app.extensions['mysql'].connection.commit()

    return jsonify({"message": "Resource added successfully"}), 201

