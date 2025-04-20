# Vaccinations API routes

from flask import Blueprint, request, jsonify, current_app
import MySQLdb.cursors






bp = Blueprint("vaccinations", __name__, url_prefix="/vaccinations")



@bp.get("", strict_slashes=False)
def get_vaccinations():
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM vaccinations")
    results = cursor.fetchall()
    return jsonify(results)


@bp.post("", strict_slashes=False)
def add_vaccination():
    data = request.get_json()

    required_fields = ["pet_id", "vaccine_name", "date_given"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    pet_id = data["pet_id"]
    vaccine_name = data["vaccine_name"]
    date_given = data["date_given"]
    veterinarian_id = data.get("veterinarian_id")
    veterinarian_name = data.get("veterinarian_name")
    next_due = data.get("next_due")

    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("""
            INSERT INTO vaccinations (pet_id, vaccine_name, date_given, veterinarian_id, veterinarian_name, next_due)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (pet_id, vaccine_name, date_given, veterinarian_id, veterinarian_name, next_due))
    current_app.extensions['mysql'].connection.commit()

    return jsonify({"message": "Vaccination added successfully"}), 201


@bp.get("/<int:vaccination_id>", strict_slashes=False)
def get_specific_vaccination(vaccination_id):
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM vaccinations WHERE vaccination_id = %s", (vaccination_id,))
    result = cursor.fetchone()
    if result:
        return jsonify(result)
    return jsonify({"error": "Vaccination not found"}), 404


@bp.delete("/<int:vaccination_id>", strict_slashes=False)
def delete_vaccination(vaccination_id):
    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute("DELETE FROM vaccinations WHERE vaccination_id = %s", (vaccination_id,))
    current_app.extensions['mysql'].connection.commit()
    return jsonify({"message": "Vaccination deleted successfully"})


@bp.put("/<int:vaccination_id>", strict_slashes=False)
def update_vaccination(vaccination_id):
    data = request.get_json()
    fields = []
    values = []

    for key in ["pet_id", "vaccine_name", "date_given", "veterinarian_id", "veterinarian_name", "next_due"]:
        if key in data:
            fields.append(f"{key} = %s")
            values.append(data[key])

    if not fields:
        return jsonify({"error": "No valid fields to update"}), 400

    values.append(vaccination_id)
    query = f"UPDATE vaccinations SET {', '.join(fields)} WHERE vaccination_id = %s"

    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute(query, tuple(values))
    current_app.extensions['mysql'].connection.commit()

    return jsonify({"message": "Vaccination updated successfully"})



from flask import Blueprint, request, jsonify, current_app
import MySQLdb.cursors

bp = Blueprint("vaccinations", __name__, url_prefix="/vaccinations")

