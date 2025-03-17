# Pets API routes

from flask import Blueprint

bp = Blueprint("pets", __name__, url_prefix="/pets")


@bp.get("", strict_slashes=False)
def get_pets():
    # TODO: return list of pets
    return []  # returning a blank list for testing


@bp.post("", strict_slashes=False)
def add_pet():
    # TODO: create a pet
    return {}


@bp.get("/<int:pet_id>", strict_slashes=False)
def get_specific_pet(pet_id):
    # TODO: return the pet that equals the pet_id
    return {}


@bp.delete("/<int:pet_id>", strict_slashes=False)
def delete_pet(pet_id):
    # TODO: delete the pet that equals the pet_id
    return {}


@bp.put("/<int:pet_id>", strict_slashes=False)
def update_pet(pet_id):
    # TODO: read the request body to get what needs to be updated for the pet
    return {}
