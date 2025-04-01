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
    # Retrieve a specific activity by ID
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM activity_logs WHERE activity_id = %s", (activity_id,))

    activity = cursor.fetchone()

    if activity:
        return jsonify(activity)
    else:
        return jsonify({"error": "Activity not found"}), 404


@bp.delete("/<int:activity_id>", strict_slashes=False)
def delete_activity(activity_id):
    # Delete an activity by ID
    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute("DELETE FROM activity_logs WHERE activity_id = %s", (activity_id,))

    if cursor.rowcount == 0:
        return jsonify({"error": "Activity not found"}), 404

    current_app.extensions['mysql'].connection.commit()
    return jsonify({"message": "Activity deleted successfully"}), 200


@bp.put("/<int:activity_id>", strict_slashes=False)
def update_activity(activity_id):
    # Update an existing activity
    data = request.json
    fields = []
    values = []

    for key in ["pet_id", "activity_type", "other_activity_type", "duration_minutes", "activity_date", "notes"]:
        if key in data:
            # Validation for ENUM field
            if key == "activity_type" and data[key] not in VALID_ACTIVITY_TYPES:
                return jsonify({"error": f"Invalid activity_type. Must be one of {VALID_ACTIVITY_TYPES}"}), 400

            # Ensure 'other_activity_type' is only used for "Other"
            if key == "other_activity_type" and data.get("activity_type") != "Other":
                continue  # Skip if activity_type is NOT "Other"

            # Ensure 'duration_minutes' is positive
            if key == "duration_minutes" and (not isinstance(data[key], int) or data[key] <= 0):
                return jsonify({"error": "duration_minutes must be a positive integer"}), 400

            fields.append(f"{key} = %s")
            values.append(data[key])

    if not fields:
        return jsonify({"error": "No fields to update"}), 400

    values.append(activity_id)
    query = f"UPDATE activity_logs SET {', '.join(fields)} WHERE activity_id = %s"

    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute(query, values)

    if cursor.rowcount == 0:
        return jsonify({"error": "Activity not found"}), 404

    current_app.extensions['mysql'].connection.commit()
    return jsonify({"message": "Activity updated successfully"}), 200
