import werkzeug.exceptions
from flask import Blueprint, render_template


errors_bp = Blueprint("errors", __name__, template_folder="templates", static_folder="static")


@errors_bp.errorhandler(404)
def error_404():
    return render_template("errors/404.html"), 404


# @errors_bp.errorhandler(flask_login.)
# def error_401():
#     return render_template("errors/404.html")


@errors_bp.errorhandler(429)
def ratelimit_handler(e):
    return "Слишком много запросов в минуту, остановитесь"
