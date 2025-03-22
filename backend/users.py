# Users API routes

from flask import Blueprint, jsonify, current_app

bp = Blueprint("users", __name__, url_prefix="/users")

# Temporary placeholder user data (to be replaced with database query later)
mock_users = {
    1: {"user_id": 1, "first_name": "John", "last_name": "Doe", "email": "john@example.com"},
    2: {"user_id": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane@example.com"}
}

@bp.get("", strict_slashes=False)
def get_users():
    # Retrieve all users (mock data for now)
    return jsonify(mock_users)

@bp.get("/test-db-connection", strict_slashes=False)
def test_db_connection():
    try:
        # Try to connect to the database and run a simple query
        cursor = current_app.extensions['mysql'].connection.cursor()
        cursor.execute("SELECT 1")
        cursor.fetchone()
        return jsonify({"status": "success", "message": "Connected to AWS RDS database successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@bp.post("", strict_slashes=False)
def add_user():
    # TODO: create a user
    return {}


@bp.get("/<int:user_id>", strict_slashes=False)
def get_specific_user(user_id):
    # TODO: return the user that equals the user_id
    return {}


@bp.delete("/<int:user_id>", strict_slashes=False)
def delete_user(user_id):
    # TODO: delete the user that equals the user_id
    return {}


@bp.put("/<int:user_id>", strict_slashes=False)
def update_user(user_id):
    # TODO: read the request body to get what needs to be updated for the user
    return {}
