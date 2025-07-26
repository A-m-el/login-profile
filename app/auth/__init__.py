from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
main_bp = Blueprint('auth', __name__)

from app.auth import routes 