from flask import (jsonify)
from app.api.base import api_bp


@api_bp.route('/health', methods=['GET'])
def health():
    try:
        return jsonify({"message": "it's alive!"})
    except Exception as e:
        return jsonify({"message": e})