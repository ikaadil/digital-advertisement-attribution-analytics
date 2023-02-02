from flask import Blueprint

event_bp = Blueprint('event_bp', __name__)


@event_bp.route('', methods=['POST'])
def create():
    pass


@event_bp.route('', methods=['GET'])
def get():
    pass
