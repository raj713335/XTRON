from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)



class PatientData(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    race = db.Column(db.String(30), nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    diastolic_bp = db.Column(db.String(10), nullable=False)
    red_blood_cells = db.Column(db.String(30), nullable=False)
    sedimentation_rate = db.Column(db.String(30), nullable=False)
    serum_albumin = db.Column(db.String(30), nullable=False)
    serum_cholestrol = db.Column(db.String(30), nullable=False)
    serum_iron = db.Column(db.String(30), nullable=False)
    serum_magnessium = db.Column(db.String(30), nullable=False)
    serum_protein = db.Column(db.String(30), nullable=False)
    systolic_bp = db.Column(db.String(30), nullable=False)
    tibc = db.Column(db.String(30), nullable=False)
    ts = db.Column(db.String(30), nullable=False)
    white_blood_cells = db.Column(db.String(30), nullable=False)
    bmi = db.Column(db.String(30), nullable=False)
    pulse_pressure = db.Column(db.String(30), nullable=False)




    def __repr__(self):
        return 'Patient Data ' + str(self.id)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')





if __name__ == "__main__":
    app.run(debug=True)
