from flask import Blueprint, request, jsonify
from extension import db
from model.user import User
from schemas.user_schema import UserSchema
from flask_jwt_extended import create_access_token

auth_bp = Blueprint("auth", __name__)
user_schema = UserSchema()

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(email=data.get("email")).first():
        return jsonify({"message": "Email already exists"}), 409
    user = User(
        name=data.get("name"),
        email=data.get("email"),
        role=data.get("role", "student")
    )
    user.password = data.get("password")  # hashed automatically
    db.session.add(user)
    db.session.commit()
    return user_schema.dump(user), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data.get("email")).first()
    if not user or not user.check_password(data.get("password")):
        return jsonify({"message": "Invalid email or password"}), 401
    token = create_access_token(identity=str(user.id), additional_claims={"role": user.role})
    return jsonify({"token": token}), 200
