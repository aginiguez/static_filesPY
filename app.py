# from petfax import create_app
# app = create_app()

from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Import and register blueprints
    from pet import bp as pet_bp
    from fact import bp as fact_bp
    
    app.register_blueprint(pet_bp)
    app.register_blueprint(fact_bp)
    
    return app
