from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100))
    voterid = db.Column(db.String(50), unique=True)
    dob = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    email = db.Column(db.String(100))
    mobile = db.Column(db.String(15))
    password = db.Column(db.String(100))

    votestatus = db.Column(db.String(20), default="Not Voted")
    candidatevoted = db.Column(db.String(100), default="Not Selected")
    votingdatetime = db.Column(db.String(100), default="Not Yet Voted")