from init import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer(),primary_key=True)
    email_address = db.Column(db.String(length=50),nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60),nullable = False)
    language = db.Column(db.String(length=60))
    age = db.Column(db.Integer())
    country = db.Column(db.String(length=100))
    tests = db.relationship('Test',backref="user",lazy=True)

class Test(db.Model):
    __tablename__ = "previous_tests"
    id = db.Column(db.Integer(),primary_key = True)
    title = db.Column(db.String(length=255), nullable = False)
    date = db.Column(db.Date)
    result = db.Column(db.String(length = 30), nullable = False)
    user_id = db.Column(db.Integer(),db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<{self.id}: {self.title}>"