from sqlalchemy import Column, Integer, String, DateTime
from config import db


class Pageview(db.Model):
    __tablename__ = 'pageviews'

    id = Column(Integer, primary_key=True)
    fingerprint = Column(String(64))
    user_id = Column(String(64))
    url = Column(String(200))
    referrer_url = Column(String(200))
    created_at = Column(DateTime)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'fingerprint': self.fingerprint,
            'user_id': self.user_id,
            'url': self.url,
            'referrer_url': self.referrer_url,
            'created_at': self.created_at
        }
