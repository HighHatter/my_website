from api import db
from datetime import datetime
from api.Tags_Blog.tag_block_table import tag_blog

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    feature_image = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'feature_image': self.feature_image,
            'created_at': self.created_at,
        }
