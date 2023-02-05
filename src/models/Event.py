from sqlalchemy import Column, Integer, String, DateTime
from config import db


class Event(db.Model):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fingerprint = Column(String(64))
    user_id = Column(String(64))
    created_at = Column(DateTime)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'fingerprint': self.fingerprint,
            'user_id': self.user_id,
            'created_at': self.created_at
        }
