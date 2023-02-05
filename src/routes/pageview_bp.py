from flask import Blueprint
from controllers.PageviewController import add, get

pageview_bp = Blueprint('pageview_bp', __name__)

pageview_bp.route('', methods=['POST'])(add)
pageview_bp.route('', methods=['GET'])(get)
