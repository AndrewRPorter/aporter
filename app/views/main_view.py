from flask import Blueprint, Response, render_template

from ..tools import crawler

main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/", methods=["GET", "POST"])
def index() -> Response:
    """Defines the main website view"""
    return render_template("index.html")


@main_bp.route("/about", methods=["GET", "POST"])
def about() -> Response:
    """Defines the view for the about section"""
    return render_template("about.html")


@main_bp.route("/photos", methods=["GET", "POST"])
def photos() -> Response:
    """Defines the view to show images"""
    images = crawler.get_images()
    return render_template("photos.html", images=images)
