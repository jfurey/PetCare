# Appointments API routes

from flask import Blueprint, jsonify, request, current_app
import MySQLdb.cursors
from datetime import timedelta


bp = Blueprint("appointments", __name__, url_prefix="/appointments")

# Define valid appointment types
VALID_APPOINTMENT_TYPES = {"Veterinarian", "Grooming", "Training", "Other"}

@bp.get("", strict_slashes=False)
def get_appointments():
    # Connect to database and retrieve all appointments
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        """
        SELECT appointment_id, pet_id, contact_id, appointment_type, other_appt_type, appointment_date,
        appointment_time, notes
        FROM appointments
        """
    )

    appointments = cursor.fetchall()

    # Convert timedelta to string for JSON serialization
    for appointment in appointments:
        if isinstance(appointment["appointment_time"], timedelta):
            appointment["appointment_time"] = str(appointment["appointment_time"])

    return jsonify(appointments)


@bp.post("", strict_slashes=False)
def add_appointment():
    # Add a new appointment
    data = request.get_json()

    required_fields = ["pet_id", "contact_id", "appointment_type", "appointment_date", "appointment_time"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    pet_id = data["pet_id"]
    contact_id = data["contact_id"]
    appointment_type = data["appointment_type"]
    other_appt_type = data.get("other_appt_type", None)
    appointment_date = data["appointment_date"]
    appointment_time = data["appointment_time"]
    notes = data.get("notes", None)

    # Validate appointment_type
    if appointment_type not in VALID_APPOINTMENT_TYPES:
        return jsonify({"error": f"Invalid appointment_type. Must be one of {list(VALID_APPOINTMENT_TYPES)}"}), 400

    # If appointment_type is not "Other", ignore other_appt_type
    if appointment_type != "Other":
        other_appt_type = None

    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute(
        "INSERT INTO appointments (pet_id, contact_id, appointment_type, other_appt_type, appointment_date, appointment_time, notes) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (pet_id, contact_id, appointment_type, other_appt_type, appointment_date, appointment_time, notes),
    )
    current_app.extensions['mysql'].connection.commit()

    return jsonify({"message": "Appointment added successfully", "appointment_id": cursor.lastrowid}), 201


@bp.get("/<int:appointment_id>", strict_slashes=False)
def get_specific_appointment(appointment_id):
    # Retrieve a specific appointment by ID
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        """
        SELECT appointment_id, pet_id, contact_id, appointment_type, other_appt_type, appointment_date,
        appointment_time, notes
        FROM appointments WHERE appointment_id = %s
        """,
        (appointment_id,)
    )

    appointment = cursor.fetchone()

    if appointment:
        if isinstance(appointment["appointment_time"], timedelta):
            appointment["appointment_time"] = str(appointment["appointment_time"])
        return jsonify(appointment)

    return jsonify({"error": "Appointment not found"}), 404


@bp.delete("/<int:appointment_id>", strict_slashes=False)
def delete_appointment(appointment_id):
    # Delete an appointment by ID
    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute("DELETE FROM appointments WHERE appointment_id = %s", (appointment_id,))
    affected_rows = cursor.rowcount
    current_app.extensions['mysql'].connection.commit()

    if affected_rows == 0:
        return jsonify({"error": "Appointment not found"}), 404
    return jsonify({"message": "Appointment deleted successfully"}), 200


@bp.put("/<int:appointment_id>", strict_slashes=False)
def update_appointment(appointment_id):
    # TODO: read the request body to get what needs to be updated for the appointment
    return {}
