from flask import Blueprint, Response, render_template

main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/", methods=["GET"])
def index() -> Response:
    """Defines the main website view"""
    return render_template("index.html")


@main_bp.route("/experience", methods=["GET"])
def experience() -> Response:
    """Defines the experience website view"""
    return render_template("experience.html")


@main_bp.route("/projects", methods=["GET", "POST"])
def projects() -> Response:
    """Defines the view to show my programming projects"""
    return render_template("projects.html")


@main_bp.route("/photography", methods=["GET", "POST"])
def photos() -> Response:
    """Defines the view to show images"""
    return render_template("photography.html", images=None)
