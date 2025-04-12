# Diets API routes

from flask import Blueprint, request, jsonify, current_app


bp = Blueprint("diets", __name__, url_prefix="/diets")


@bp.get("", strict_slashes=False)
def get_diets():
    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM diets")
    diets = cursor.fetchall()
    cursor.close()
    return jsonify(diets)


@bp.post("", strict_slashes=False)
def add_diet():
    data = request.json
    pet_id = data.get("pet_id")
    food_name = data.get("food_name")
    amount = data.get("amount")
    frequency = data.get("frequency")

    if not (pet_id and food_name and amount and frequency):
        return jsonify({"error": "Missing required fields"}), 400

    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO diets (pet_id, food_name, amount, frequency) VALUES (%s, %s, %s, %s)",
        (pet_id, food_name, amount, frequency)
    )
    mysql.connection.commit()
    new_id = cursor.lastrowid
    cursor.close()

    return jsonify({"id": new_id, "pet_id": pet_id, "food_name": food_name, "amount": amount, "frequency": frequency}), 201


@bp.get("/<int:diet_id>", strict_slashes=False)
def get_specific_diet(diet_id):
    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM diets WHERE id = %s", (diet_id,))
    diet = cursor.fetchone()
    cursor.close()

    if diet:
        return jsonify(diet)
    else:
        return jsonify({"error": "Diet not found"}), 404


@bp.delete("/<int:diet_id>", strict_slashes=False)
def delete_diet(diet_id):
    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM diets WHERE id = %s", (diet_id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"message": "Diet deleted"}), 204


@bp.put("/<int:diet_id>", strict_slashes=False)
def update_diet(diet_id):
    data = request.json
    food_name = data.get("food_name")
    amount = data.get("amount")
    frequency = data.get("frequency")

    if not (food_name and amount and frequency):
        return jsonify({"error": "Missing required fields"}), 400

    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute(
        "UPDATE diets SET food_name = %s, amount = %s, frequency = %s WHERE id = %s",
        (food_name, amount, frequency, diet_id)
    )
    mysql.connection.commit()
    cursor.close()

    return jsonify({"id": diet_id, "food_name": food_name, "amount": amount, "frequency": frequency})
