from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    original_password = db.Column(db.String(200)) 
    feedback_given = db.Column(db.Integer, default=0)
    reports_generated = db.Column(db.Integer, default=0)
    profile_pic = db.Column(db.String(200), nullable=True)

    
class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_no = db.Column(db.String(20))
    row_no = db.Column(db.Integer, nullable=True)
    filename = db.Column(db.String(255))
    content_type = db.Column(db.String(50))
    file_data = db.Column(db.LargeBinary)
    session_id = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='uploaded_files')

    
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(120))  # e.g. "project_report"
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('submissions', lazy=True))

