from flask import Blueprint, request, jsonify, current_app
import MySQLdb.cursors

bp = Blueprint("medications", __name__, url_prefix="/medications")


@bp.get("", strict_slashes=False)
def get_medications():
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM medications")
    results = cursor.fetchall()
    return jsonify(results)


@bp.get("/<int:medication_id>", strict_slashes=False)
def get_specific_medication(medication_id):
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM medications WHERE medication_id = %s", (medication_id,))
    result = cursor.fetchone()
    if result:
        return jsonify(result)
    return jsonify({"error": "Medication not found"}), 404


@bp.post("", strict_slashes=False)
def add_medication():
    data = request.get_json()

    required_fields = ["pet_id", "medication_name", "dosage", "start_date"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    pet_id = data["pet_id"]
    medication_name = data["medication_name"]
    dosage = data["dosage"]
    start_date = data["start_date"]
    frequency = data.get("frequency")
    end_date = data.get("end_date")
    prescribed_by = data.get("prescribed_by")

    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute("""
        INSERT INTO medications (pet_id, medication_name, dosage, frequency, start_date, end_date, prescribed_by)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (pet_id, medication_name, dosage, frequency, start_date, end_date, prescribed_by))
    current_app.extensions['mysql'].connection.commit()

    return jsonify({"message": "Medication added successfully"}), 201


@bp.put("/<int:medication_id>", strict_slashes=False)
def update_medication(medication_id):
    data = request.get_json()
    fields = []
    values = []

    for key in ["pet_id", "medication_name", "dosage", "frequency", "start_date", "end_date", "prescribed_by"]:
        if key in data:
            fields.append(f"{key} = %s")
            values.append(data[key])

    if not fields:
        return jsonify({"error": "No valid fields to update"}), 400

    values.append(medication_id)
    query = f"UPDATE medications SET {', '.join(fields)} WHERE medication_id = %s"

    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute(query, tuple(values))
    current_app.extensions['mysql'].connection.commit()

    return jsonify({"message": "Medication updated successfully"})


@bp.delete("/<int:medication_id>", strict_slashes=False)
def delete_medication(medication_id):
    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute("DELETE FROM medications WHERE medication_id = %s", (medication_id,))
    current_app.extensions['mysql'].connection.commit()
    return jsonify({"message": "Medication deleted successfully"})


@bp.get("/pet/<int:pet_id>", strict_slashes=False)
def get_medications_by_pet(pet_id):
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM medications WHERE pet_id = %s", (pet_id,))
    results = cursor.fetchall()
    return jsonify(results)
