from flask import Flask
from routes import ai_routes  # Import your routes

def create_app():
    app = Flask(__name__)

    # Register blueprints or routes
    app.register_blueprint(ai_routes.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
