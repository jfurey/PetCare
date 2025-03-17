# Users API routes

from flask import Blueprint

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.get("", strict_slashes=False)
def get_users():
    # TODO: return list of users
    return []  # returning a blank list for testing


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
