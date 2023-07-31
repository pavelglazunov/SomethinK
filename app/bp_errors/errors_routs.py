from flask import Blueprint, render_template, request
from app import application

errors_bp = Blueprint("errors", __name__, template_folder="templates", static_folder="static")


@errors_bp.errorhandler(404)
def error_404():
    return render_template("errors/404.html"), 404


@errors_bp.errorhandler(429)
def ratelimit_handler(e):
    return "Слишком много запросов в минуту, остановитесь"


@errors_bp.errorhandler(500)
def handle_error(error):
    application.logger.exception('Unhandled Exception: %s', error, extra={'stack': True, 'data': {'request': request}})
    return 'Internal Server Error', 500