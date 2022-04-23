from api import db

class Tag(db.Model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(30))
    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name
        }

