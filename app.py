from flask import Flask, render_template, request
from flask_migrate import Migrate
from models import db, Voter

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/votedb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# Create database table
with app.app_context():
    db.create_all()


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("bootstrapmenu.html")


# ---------------- REGISTRATION PAGE ----------------
@app.route("/register", methods=["GET"])
def register_page():
    return render_template("voting.html")


# ---------------- SAVE REGISTRATION ----------------
@app.route("/register", methods=["POST"])
def register():

    voter = Voter(
        fullname=request.form["fullname"],
        voterid=request.form["voterid"],
        dob=request.form["dob"],
        gender=request.form["gender"],
        email=request.form["email"],
        mobile=request.form["mobile"],
        password=request.form["password"],
        votestatus="Not Voted",
        candidatevoted="Not Selected",
        votingdatetime="Not Yet Voted"
    )

    db.session.add(voter)
    db.session.commit()

    return '''
    <script>
        alert("Voter Registered Successfully");
        window.location.href="/voter/list";
    </script>
    '''


# ---------------- VOTER TABLE ----------------
@app.route("/voter/list")
def voter_list():

    voters = Voter.query.all()

    return render_template("bootstraptable.html", voters=voters)


# ---------------- LOGIN PAGE ----------------
@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)