from flask import Flask, jsonify
from extension import db, ma, jwt
from config import *
from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from model import *  # import all models

# Initialize Flask app
app = Flask(__name__)
app.config.from_object("config")

# Initialize extensions
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(user_bp, url_prefix='/users')

# Root route to check server
@app.route('/')
def home():
    return {"message": "Server is running successfully"}

# Optional: test route
@app.route('/test')
def test():
    return {"message": "Flask is running"}

# Create tables on startup
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    # Run the server on port 5000
    app.run(debug=True, port=5000)
