from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)

# ─────────────────────────────────────────
# Health check — required on every service
# ─────────────────────────────────────────
@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "template-service"}), 200


# ─────────────────────────────────────────
# Add your routes below
# Follow this exact response envelope:
#
# Success: {"code": 200, "data": {...},  "message": "success"}
# Error:   {"code": 4xx, "data": null,   "message": "description"}
# ─────────────────────────────────────────

def success_response(data, code=200, message="success"):
    return jsonify({"code": code, "data": data, "message": message}), code

def error_response(message, code=400):
    return jsonify({"code": code, "data": None, "message": message}), code
    