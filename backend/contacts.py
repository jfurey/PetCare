# Contacts API routes

from flask import Blueprint, request, jsonify
from flask_mysqldb import MySQL

bp = Blueprint("contacts", __name__, url_prefix="/contacts")
mysql = MySQL()

@bp.get("", strict_slashes=False)
def get_contacts():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()
    cur.close()
    return jsonify(contacts)

@bp.post("", strict_slashes=False)
def add_contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Contact added successfully"}), 201

@bp.get("/<int:contact_id>", strict_slashes=False)
def get_specific_contact(contact_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM contacts WHERE contact_id = %s", (contact_id,))
    contact = cur.fetchone()
    cur.close()
    return jsonify(contact)

@bp.delete("/<int:contact_id>", strict_slashes=False)
def delete_contact(contact_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM contacts WHERE contact_id = %s", (contact_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Contact deleted"})

@bp.put("/<int:contact_id>", strict_slashes=False)
def update_contact(contact_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE contacts SET name = %s, email = %s, phone = %s WHERE contact_id = %s",
        (name, email, phone, contact_id)
    )
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Contact updated"})