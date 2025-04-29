# Notifications API routes

from flask import Blueprint, jsonify, request, current_app
import MySQLdb.cursors

bp = Blueprint("notifications", __name__, url_prefix="/notifications")


@bp.get("", strict_slashes=False)
def get_notifications():
    # Get all notifications for a user (expects 'user_id' as query param).
    # Example: GET /notifications?user_id=123
    user_id = request.args.get('user_id', type=int)
    if not user_id:
        return jsonify({"error": "Missing required query parameter: user_id"}), 400

    cursor = current_app.extensions['mysql'].connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        """
        SELECT notification_id, user_id, pet_id, type, title, message, is_read, created_at
        FROM notifications
        WHERE user_id = %s
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    notifications = cursor.fetchall()
    return jsonify(notifications)


@bp.post("", strict_slashes=False)
def create_notification():
    # Create a new notification.
    data = request.get_json()

    required_fields = ["user_id", "type", "title", "message"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    user_id = data["user_id"]
    pet_id = data.get("pet_id")  # Optional
    type_ = data["type"]
    title = data["title"]
    message = data["message"]

    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute(
        """
        INSERT INTO notifications (user_id, pet_id, type, title, message)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (user_id, pet_id, type_, title, message)
    )
    current_app.extensions['mysql'].connection.commit()

    return jsonify({"message": "Notification created successfully", "notification_id": cursor.lastrowid}), 201


@bp.patch("/<int:notification_id>/read", strict_slashes=False)
def mark_notification_as_read(notification_id):
    # Mark a notification as read.
    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute(
        """
        UPDATE notifications
        SET is_read = TRUE
        WHERE notification_id = %s
        """,
        (notification_id,)
    )
    affected_rows = cursor.rowcount
    current_app.extensions['mysql'].connection.commit()

    if affected_rows == 0:
        return jsonify({"error": "Notification not found"}), 404

    return jsonify({"message": "Notification marked as read"}), 200


@bp.delete("/<int:notification_id>", strict_slashes=False)
def delete_notification(notification_id):
    # Delete a notification by ID.
    cursor = current_app.extensions['mysql'].connection.cursor()
    cursor.execute("DELETE FROM notifications WHERE notification_id = %s", (notification_id,))
    affected_rows = cursor.rowcount
    current_app.extensions['mysql'].connection.commit()

    if affected_rows == 0:
        return jsonify({"error": "Notification not found"}), 404

    return jsonify({"message": "Notification deleted successfully"}), 200
