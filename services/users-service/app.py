import os
from flask import Flask
from extensions import db
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# ─────────────────────────────────────────
# Database config
# ─────────────────────────────────────────
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# ─────────────────────────────────────────
# Register routes
# ─────────────────────────────────────────
from routes import bp
app.register_blueprint(bp)

# ─────────────────────────────────────────
# Create tables on startup
# ─────────────────────────────────────────
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    app.run(host="0.0.0.0", port=port, debug=False)