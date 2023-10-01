from flask import Flask


def create_app():
    print("create_app called!")
    app = Flask(__name__)
    
    # Register blueprints here
    # blueprint for main app
    from app.main import bp as main_bp # import blueprint 
    app.register_blueprint(main_bp) # register blueprint

    return app