from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from model.user import User
from schemas.user_schema import UserSchema

# 1️⃣ Define blueprint FIRST
user_bp = Blueprint("users", __name__)
user_schema = UserSchema()  # single user schema
user_schema_many = UserSchema(many=True)

# 2️⃣ Admin-only helper
from flask_jwt_extended import get_jwt
def admin_only():
    claims = get_jwt()
    return claims.get("role") == "admin"

# 3️⃣ Routes

# Admin: get all users
@user_bp.route("/get_all", methods=["GET"])
@jwt_required()
def get_all():
    if not admin_only():
        return jsonify({"message": "Admin access required"}), 403
    users = User.query.all()
    return user_schema_many.dump(users), 200

# Any user: get current user info
@user_bp.route("/me", methods=["GET"])
@jwt_required()
def get_current_user():
    user_id = get_jwt_identity()  # gets logged-in user ID from JWT
    user = User.query.get(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return user_schema.dump(user), 200
