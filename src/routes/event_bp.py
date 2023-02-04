from flask import Blueprint
from controllers.EventController import add, get


event_bp = Blueprint('event_bp', __name__)

event_bp.route('', methods=['POST'])(add)
event_bp.route('', methods=['GET'])(get)
