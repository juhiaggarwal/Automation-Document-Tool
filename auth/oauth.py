from flask_dance.contrib.google import make_google_blueprint
from flask_dance.contrib.linkedin import make_linkedin_blueprint

def create_oauth_blueprints(app):
    google_bp = make_google_blueprint(
        client_id=app.config['GOOGLE_OAUTH_CLIENT_ID'],
        client_secret=app.config['GOOGLE_OAUTH_CLIENT_SECRET'],
        redirect_to="google_login"
    )
    linkedin_bp = make_linkedin_blueprint(
        client_id=app.config['LINKEDIN_OAUTH_CLIENT_ID'],
        client_secret=app.config['LINKEDIN_OAUTH_CLIENT_SECRET'],
        redirect_to="linkedin_login"
    )
    app.register_blueprint(google_bp, url_prefix="/login")
    app.register_blueprint(linkedin_bp, url_prefix="/login")
