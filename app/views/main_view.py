from flask import Blueprint, Response, render_template

main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/", methods=["GET", "POST"])
def index() -> Response:
    """
    Defines the main website view
    """
    return render_template("index.html")
