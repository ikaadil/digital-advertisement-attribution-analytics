from flask import Blueprint
from controllers.PageviewController import add

pageview_bp = Blueprint('pageview_bp', __name__)

pageview_bp.route('', methods=['POST'])(add)
