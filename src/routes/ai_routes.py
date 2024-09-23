from flask import Blueprint, jsonify

bp = Blueprint("ai_routes", __name__)

@bp.route("/ai", methods=["GET"])
def get_users():
    return jsonify({"users": ["Alice", "Bob"]})



@bp.route("/get-all-ais", methods=["GET"])
def get_all_ais():
    return jsonify({
        "ai-1": {
            "name": "TesteAi"
        },
        "ai-2": {
            "name": "TesteAi2"
        },
        "ai-3": {
            "name": "TesteAi3"
        }
    });