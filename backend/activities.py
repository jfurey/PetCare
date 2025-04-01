# Activities API routes

from flask import Blueprint, jsonify, request, current_app
import MySQLdb.cursors

bp = Blueprint("activities", __name__, url_prefix="/activities")

# Valid ENUM values for activity_type
VALID_ACTIVITY_TYPES = {"Walk", "Run", "Play", "Other"}

@bp.get("", strict_slashes=False)
def get_activities():
    # Connect to database and retrieve activities
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
            """
            SELECT activity_id, pet_id, activity_type, other_activity_type, duration_minutes, activity_date, notes
            FROM activity_logs
            """
    )

    activity_list = cursor.fetchall()
    return jsonify(activity_list)


@bp.post("", strict_slashes=False)
def add_activity():
    # Create a new activity
    data = request.json
    pet_id = data.get("pet_id")
    activity_type = data.get("activity_type")
    other_activity_type = data.get("other_activity_type", None)
    duration_minutes = data.get("duration_minutes")
    activity_date = data.get("activity_date", None)
    notes = data.get("notes", None)

    # Validate required fields
    if not pet_id or not activity_type or duration_minutes is None:
        return jsonify({"error": "Missing required fields"}), 400

    # Validate activity_type
    if activity_type not in VALID_ACTIVITY_TYPES:
        return jsonify({"error": f"Invalid activity_type. Must be one of {VALID_ACTIVITY_TYPES}"}), 400

    # Ensure other_activity_type is only used when activity_type = 'Other'
    if activity_type != "Other":
        other_activity_type = None

    # Ensure duration_minutes is a positive integer
    if not isinstance(duration_minutes, int) or duration_minutes <= 0:
        return jsonify({"error": "duration_minutes must be a positive integer"}), 400

    # Insert into the database
    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute(
        """
        INSERT INTO activity_logs (pet_id, activity_type, other_activity_type, duration_minutes, activity_date, notes)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (pet_id, activity_type, other_activity_type, duration_minutes, activity_date, notes)
    )
    current_app.extensions['mysql'].connection.commit()

    return jsonify({"message": "Activity added successfully"}), 201


@bp.get("/<int:activity_id>", strict_slashes=False)
def get_specific_activity(activity_id):
    # TODO: return the activity that equals the activity_id
    return {}


@bp.delete("/<int:activity_id>", strict_slashes=False)
def delete_activity(activity_id):
    # TODO: delete the activity that equals the activity_id
    return {}


@bp.put("/<int:activity_id>", strict_slashes=False)
def update_activity(activity_id):
    # TODO: read the request body to get what needs to be updated for the activity
    return {}
