from flask import Blueprint, jsonify, request
from app import db
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from datetime import datetime

bp = Blueprint("main", __name__)

# ─────────────────────────────────────────
# Helper responses
# ─────────────────────────────────────────
def success_response(data, code=200, message="success"):
    return jsonify({"code": code, "data": data, "message": message}), code

def error_response(message, code=400):
    return jsonify({"code": code, "data": None, "message": message}), code


# ─────────────────────────────────────────
# Health check
# ─────────────────────────────────────────
@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "users-service"}), 200


# ─────────────────────────────────────────
# POST /api/users/register
# Create a new user account
# ─────────────────────────────────────────
@bp.route("/api/users/register", methods=["POST"])
def register():
    data = request.get_json()

    # Check all required fields are present
    required = ["full_name", "email", "password", "phone_number", "role"]
    for field in required:
        if field not in data:
            return error_response(f"Missing field: {field}", 400)

    # Check role is valid
    if data["role"] not in ["guest", "host"]:
        return error_response("Role must be guest or host", 400)

    # Check email is not already registered
    existing = User.query.filter_by(email=data["email"]).first()
    if existing:
        return error_response("Email already registered", 409)

    # Create new user
    new_user = User(
        id           = str(uuid.uuid4()),
        full_name    = data["full_name"],
        email        = data["email"],
        password     = generate_password_hash(data["password"]),
        phone_number = data["phone_number"],
        role         = data["role"],
        created_at   = datetime.utcnow()
    )

    db.session.add(new_user)
    db.session.commit()

    return success_response({
        "id":           new_user.id,
        "full_name":    new_user.full_name,
        "email":        new_user.email,
        "phone_number": new_user.phone_number,
        "role":         new_user.role,
        "created_at":   new_user.created_at.isoformat()
    }, 201, "User registered successfully")


# ─────────────────────────────────────────
# POST /api/users/login
# Verify email and password
# ─────────────────────────────────────────
@bp.route("/api/users/login", methods=["POST"])
def login():
    data = request.get_json()

    if "email" not in data or "password" not in data:
        return error_response("Email and password required", 400)

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return error_response("Invalid email or password", 401)

    return success_response({
        "id":           user.id,
        "full_name":    user.full_name,
        "email":        user.email,
        "phone_number": user.phone_number,
        "role":         user.role
    })


# ─────────────────────────────────────────
# GET /api/users/<user_id>
# Fetch a user profile by ID
# ─────────────────────────────────────────
@bp.route("/api/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return error_response("User not found", 404)

    return success_response({
        "id":           user.id,
        "full_name":    user.full_name,
        "email":        user.email,
        "phone_number": user.phone_number,
        "role":         user.role,
        "created_at":   user.created_at.isoformat()
    })