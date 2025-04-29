# Diet Logs API routes

from flask import Blueprint, request, jsonify, current_app
import MySQLdb.cursors
from datetime import datetime

bp = Blueprint("diets", __name__, url_prefix="/diets")


@bp.get("", strict_slashes=False)
def get_diet_logs():
    try:
        mysql = current_app.extensions['mysql']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM diet_logs")
        diet_logs = cursor.fetchall()
        cursor.close()
        return jsonify(diet_logs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.post("", strict_slashes=False)
def add_diet_log():
    try:
        data = request.json
        pet_id = data.get("pet_id")
        food_name = data.get("food_name")
        quantity = data.get("quantity")
        meal_time = data.get("meal_time", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        notes = data.get("notes", "")

        if not (pet_id and food_name and quantity):
            return jsonify({"error": "Missing required fields: pet_id, food_name, quantity"}), 400

        mysql = current_app.extensions['mysql']
        cursor = mysql.connection.cursor()
        cursor.execute(
            "INSERT INTO diet_logs (pet_id, food_name, quantity, meal_time, notes, created_at) VALUES (%s, %s, %s, %s, %s, NOW())",
            (pet_id, food_name, quantity, meal_time, notes)
        )
        mysql.connection.commit()
        new_id = cursor.lastrowid
        cursor.close()

        return jsonify({
            "diet_id": new_id,
            "pet_id": pet_id,
            "food_name": food_name,
            "quantity": quantity,
            "meal_time": meal_time,
            "notes": notes
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.get("/<int:diet_id>", strict_slashes=False)
def get_specific_diet_log(diet_id):
    try:
        mysql = current_app.extensions['mysql']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM diet_logs WHERE diet_id = %s", (diet_id,))
        diet_log = cursor.fetchone()
        cursor.close()

        if diet_log:
            return jsonify(diet_log)
        else:
            return jsonify({"error": "Diet log not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.delete("/<int:diet_id>", strict_slashes=False)
def delete_diet_log(diet_id):
    try:
        mysql = current_app.extensions['mysql']
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM diet_logs WHERE diet_id = %s", (diet_id,))
        mysql.connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()

        if affected_rows > 0:
            return jsonify({"message": "Diet log deleted"}), 200
        else:
            return jsonify({"error": "Diet log not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.put("/<int:diet_id>", strict_slashes=False)
def update_diet_log(diet_id):
    try:
        data = request.json
        update_fields = []
        values = []

        for field in ["pet_id", "food_name", "quantity", "meal_time", "notes"]:
            if field in data:
                update_fields.append(f"{field} = %s")
                values.append(data.get(field))

        if not update_fields:
            return jsonify({"error": "No valid fields to update"}), 400

        values.append(diet_id)
        query = f"UPDATE diet_logs SET {', '.join(update_fields)} WHERE diet_id = %s"

        mysql = current_app.extensions['mysql']
        cursor = mysql.connection.cursor()
        cursor.execute(query, tuple(values))
        mysql.connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()

        if affected_rows > 0:
            return jsonify({"message": "Diet log updated successfully"})
        else:
            return jsonify({"error": "Diet log not found or no changes made"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.get("/pet/<int:pet_id>", strict_slashes=False)
def get_diet_logs_by_pet(pet_id):
    try:
        mysql = current_app.extensions['mysql']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM diet_logs WHERE pet_id = %s ORDER BY meal_time DESC", (pet_id,))
        diet_logs = cursor.fetchall()
        cursor.close()

        return jsonify(diet_logs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500