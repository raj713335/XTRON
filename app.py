
try:
    from flask import Flask
    from flask import redirect,url_for,request,render_template
    from flask_wtf.file import FileField 
    from wtforms import SubmitField
    from flask_wtf import Form
    import sqlite3
    from datetime import datetime
    print("All Modules Loaded properly ....")
except:
    print("Some Modules are missing ....")




app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret'

class Upload_Chest_Xray(Form):
    file=FileField()
    submit = SubmitField("submit")


def patient_database(name,filename,data):
    conn=sqlite3.connect("PATIENT_DB")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS PATIENT_TABLE (name TEXT,filename TEXT,data BLOB)""")
    cursor.execute("""INSERT INTO PATIENT_TABLE (name,filename,data) VALUES (?,?,?) """,(name,filename,data))
    conn.commit()
    cursor.close()
    conn.close()





# class PatientData(db.Model):
#     p_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(30), nullable=False)
#     age = db.Column(db.Integer(30), nullable=False)
#     race = db.Column(db.String(30), nullable=False)
#     sex = db.Column(db.String(10), nullable=False)
#     diastolic_bp = db.Column(db.Integer(10), nullable=False)
#     red_blood_cells = db.Column(db.Integer(30), nullable=False)
#     sedimantation_rate = db.Column(db.Integer(30), nullable=False)
#     serum_albumin = db.Column(db.Integer(30), nullable=False)
#     serum_cholestrol = db.Column(db.Integer(30), nullable=False)
#     serum_iron = db.Column(db.Integer(30), nullable=False)
#     serum_magnesium = db.Column(db.Integer(30), nullable=False)
#     serum_protein = db.Column(db.Integer(30), nullable=False)
#     systolic_bp = db.Column(db.Integer(30), nullable=False)
#     tibc = db.Column(db.Integer(30), nullable=False)
#     ts = db.Column(db.Integer(30), nullable=False)
#     white_blood_cells = db.Integer(db.String(30), nullable=False)
#     bmi = db.Column(db.Integer(30), nullable=False)
#     pulse_pressure = db.Column(db.Integer(30), nullable=False)
#     date_time=db.Column(db.)
#
#
#
#
#    def __repr__(self):
#        return 'Patient Data ' + str(self.id)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form',methods=["GET","POST"])
def form():
    form = Upload_Chest_Xray()
    if request.method=="POST":
        if form.validate_on_submit():
            name=form.file.data
            file_name=form.file.data

            patient_database(name=name.filename,filename=file_name.filename,data=file_name.read())
            print("FILE : {}".format((file_name.filename)))
            return render_template('form.html',form=form)
    return render_template('form.html',form=form)





if __name__ == "__main__":
    app.run(debug=True)
