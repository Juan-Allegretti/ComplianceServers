from flask import Blueprint


bp = Blueprint("ping", __name__)


@bp.route("/a")
def main():
    return "pong"


@bp.route("/b")
def asd():
    return "b"