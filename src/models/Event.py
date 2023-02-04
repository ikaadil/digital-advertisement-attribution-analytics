from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    fingerprint = db.Column(db.String(64))
    user_id = db.Column(db.String(64))
    created_at = db.Column(db.DateTime)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'fingerprint': self.fingerprint,
            'user_id': self.user_id,
            'created_at': self.created_at
        }
