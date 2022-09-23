from flask import Blueprint, jsonify

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    return jsonify({
        'status': 'running...'
    })