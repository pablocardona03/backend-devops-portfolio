from flask import Blueprint, jsonify, request, render_template
from app import mysql
import re

main = Blueprint('main', __name__)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return render_template('users.html', users=users)

@main.route('/users/<int:user_id>/edit', methods=['GET'], endpoint='edit_user')
def edit_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()

    if user:
        return render_template('edit_user.html', user=user)
    return "User not found", 404

@main.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'User successfully created'}), 201
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@main.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400

    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    try:
        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
        mysql.connection.commit()
        cur.close()
        return render_template('users.html', users=get_all_users())  # o redirige
    except Exception as e:
        return f"Server error: {str(e)}", 500
    
    
def get_all_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return users   

@main.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()

        if not user:
            return jsonify({'error': 'User not found'}), 404

        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'User successfully deleted'}), 200
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500
