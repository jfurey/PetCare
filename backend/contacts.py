# Contacts API routes

from flask import Blueprint, request, jsonify, current_app


bp = Blueprint("contacts", __name__, url_prefix="/contacts")

@bp.get("", strict_slashes=False)
def get_contacts():
    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contacts")
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)


@bp.post("", strict_slashes=False)
def add_contact():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Missing required fields"}), 400

    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO contacts (name, email) VALUES (%s, %s)", (name, email))
    mysql.connection.commit()
    new_id = cursor.lastrowid
    cursor.close()

    return jsonify({"id": new_id, "name": name, "email": email}), 201


@bp.get("/<int:contact_id>", strict_slashes=False)
def get_specific_contact(contact_id):
    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM contacts WHERE id = %s", (contact_id,))
    result = cursor.fetchone()
    cursor.close()

    if not result:
        return jsonify({"error": "Contact not found"}), 404

    return jsonify(result)


@bp.delete("/<int:contact_id>", strict_slashes=False)
def delete_contact(contact_id):
    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = %s", (contact_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"message": "Contact deleted"}), 204


@bp.put("/<int:contact_id>", strict_slashes=False)
def update_contact(contact_id):
    data = request.json
    name = data.get("name")
    email = data.get("email")

    if not name or not email:
        return jsonify({"error": "Missing required fields"}), 400

    mysql = current_app.extensions['mysql']
    cursor = mysql.connection.cursor()
    cursor.execute(
        "UPDATE contacts SET name = %s, email = %s WHERE id = %s",
        (name, email, contact_id)
    )
    mysql.connection.commit()
    cursor.close()

    return jsonify({"id": contact_id, "name": name, "email": email})
