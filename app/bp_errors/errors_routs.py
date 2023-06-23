from flask import Blueprint

errors_bp = Blueprint("errors", __name__, template_folder="templates", static_folder="static")


@errors_bp.errorhandler(429)
def ratelimit_handler(e):
    return "Слишком дохуя запросов в минуту, остановитесь"
