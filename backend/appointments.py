# Appointments API routes

from flask import Blueprint, jsonify, request, current_app
import MySQLdb.cursors

bp = Blueprint("appointments", __name__, url_prefix="/appointments")


@bp.get("", strict_slashes=False)
def get_appointments():
    # connect to database and retrieve activities
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT appointment_id, pet_id, contact_id, appointment_type, other_appt_type, appointment_date, appointment_time, notes FROM appointments")

    appointment_list = cursor.fetchall()

    #convert to dictionary
    appointments = {appointment['appointment_id']: appointment for appointment in appointment_list}
    return jsonify(appointments)


@bp.post("", strict_slashes=False)
def add_appointment():
    # TODO: create a appointment
    return {}


@bp.get("/<int:appointment_id>", strict_slashes=False)
def get_specific_appointment(appointment_id):
    # TODO: return the appointment that equals the appointment_id
    return {}


@bp.delete("/<int:appointment_id>", strict_slashes=False)
def delete_appointment(appointment_id):
    # TODO: delete the appointment that equals the appointment_id
    return {}


@bp.put("/<int:appointment_id>", strict_slashes=False)
def update_appointment(appointment_id):
    # TODO: read the request body to get what needs to be updated for the appointment
    return {}
