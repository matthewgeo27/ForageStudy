from flask import Blueprint, request, jsonify
# Adjust this import based on where your createAccount function actually lives
from backend.services.accountServices import createAccount 

# Define the Blueprint
# "account_api" is the internal name, __name__ helps locate resources
account_bp = Blueprint('account_api', __name__)

@account_bp.route('/register', methods=['POST'])
def register_user():
    # 1. Get JSON data from the request body
    data = request.get_json()
    
    # 2. Extract fields (add safety checks if needed)
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    # 3. Call your service logic
    new_user = createAccount(username, email, password)

    # 4. Return appropriate response
    if new_user:
        return jsonify({
            "message": "User created successfully", 
            "user_id": new_user.id
        }), 201
    else:
        return jsonify({
            "error": "User already exists or creation failed"
        }), 400