from flask import Blueprint, Response, render_template

from ..tools import crawler

main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/", methods=["GET", "POST"])
def index() -> Response:
    """Defines the main website view"""
    return render_template("index.html")


@main_bp.route("/projects", methods=["GET", "POST"])
def projects() -> Response:
    """Defines the view to show my programming projects"""
    return render_template("projects.html")


@main_bp.route("/photography", methods=["GET", "POST"])
def photos() -> Response:
    """Defines the view to show images"""
    images = crawler.get_images()
    return render_template("photography.html", images=images)
