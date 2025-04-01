# Activities API routes

from flask import Blueprint, jsonify, request, current_app
import MySQLdb.cursors

bp = Blueprint("activities", __name__, url_prefix="/activities")


@bp.get("", strict_slashes=False)
def get_activities():
    # connect to database and retrieve activities
    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT activity_id, pet_id, activity_type, other_activity_type, duration_minutes, activity_date, notes FROM activity_logs")

    activity_list = cursor.fetchall()

    # convert to dictionary
    activities = {activity['activity_id']: activity for activity in activity_list}
    return jsonify(activities)


@bp.post("", strict_slashes=False)
def add_activity():
    # TODO: create an activity
    return {}


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
