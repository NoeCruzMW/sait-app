from app import db

class Company(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.String(100), nullable=False)
    users = db.Column(db.String(256), nullable=False)
    creation = db.Column(db.String(256), nullable=False)
    image = db.Column(db.String(256), nullable=False)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit();

    