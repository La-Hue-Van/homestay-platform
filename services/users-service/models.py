from extensions import db
from datetime import datetime
import uuid

class User(db.Model):
    __tablename__ = "users"

    id           = db.Column(db.String(36),  primary_key=True, default=lambda: str(uuid.uuid4()))
    full_name    = db.Column(db.String(255), nullable=False)
    email        = db.Column(db.String(255), nullable=False, unique=True)
    password     = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20),  nullable=False)
    role         = db.Column(db.String(10),  nullable=False)
    created_at   = db.Column(db.DateTime,    nullable=False, default=datetime.utcnow)