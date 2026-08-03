"""
=========================================================
AlgoPipX Educational Assistant
Main Entry Point
=========================================================
"""

from aiohttp import web

from webhook import (
    create_app
)

from config import PORT


def main():
    """
    Starts the aiohttp web server.
    """

    app = create_app()

    web.run_app(
        app,
        host="0.0.0.0",
        port=PORT
    )


if __name__ == "__main__":
    main()
