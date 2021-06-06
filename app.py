# Import modules
from flask import Flask,render_template,request,flash,session
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, FloatField, validators
import random
import mysql.connector
import pymysql
pymysql.install_as_MySQLdb()

# Database connectivity
app=Flask(__name__)
app.secret_key="super-secret-key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/app_assign'
db=SQLAlchemy(app)


#Retrieve columns of database into python file 
class Student(db.Model):
	Sno=db.Column(db.Integer,primary_key=True)
	Name=db.Column(db.String(80),nullable=False)
	student_id=db.Column(db.Integer,nullable=False)
	Dob=db.Column(db.String(80))
	Email=db.Column(db.String(80),nullable=False)
	Username=db.Column(db.String(80),nullable=False)
	Password=db.Column(db.String(80),nullable=False)


class InputForm(Form):
    n1 = FloatField(validators=[validators.InputRequired()])

	
# Login page
@app.route('/',methods=['GET','POST'])
def login():
	return render_template('login.html')
	session.pop('user')

# Registered page
@app.route('/register',methods=['GET','POST'])
def register():
	return render_template('register.html')


@app.route('/validations',methods=['GET','POST'])
def validations():
	ex=""
	flag=0
	ex=Student().query.all()
	n2=random.randint(1,999)




	if request.method=='POST':
		# from login page
		user1=request.form.get('username')
		password1=request.form.get('password')
		
	
		for i in ex:
			if i.Username==user1 and i.Password==password1:
				n=i.Name
				student_id=i.student_id
				id_tag=n2
				d=i.Dob
				e=i.Email
				session['user']=user1
				flag=1
				break
			elif i.Username==user1 and i.Password!=password1:
				flag=2
				break

	if flag==1:
		id_tag=request.form.get('n2')
		id_tag=n2
		mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="app_assign"
		)

		mycursor = mydb.cursor()

		sql = """UPDATE student SET id_tag = %s WHERE student_id= %s"""
		data=(id_tag,student_id)
		mycursor.execute(sql,data)

		mydb.commit()
		return render_template("home.html",name=n,student_id=student_id,id_tag=n2)

	elif flag==2:
		flash("Incorrect password.Try again.....")
		return render_template("login.html")
	else: 
		flash("User is not registered...please signup")
		return render_template("login.html")



@app.route('/registeration',methods=['GET','POST'])

def registeration():
	if (request.method=='POST'):
		name2=request.form.get('name')
		student_id2=request.form.get('student_id')
		date2=request.form.get('dob')
		email2=request.form.get('email')
		username2=request.form.get('username')
		password2=request.form.get('password')


		ex=""
		flag=0
		ex=Student().query.all()
		for i in ex:
			if i.Username==username2:
				flag=1
				break
			elif i.Email==email2:
				flag=2
				break


		if flag==1:
			flash('Username is already in use')
			return render_template('register.html')
		elif flag==2:
			flash('Email is already in use')
			return render_template('register.html')
		else:
			entry=Student(Name=name2,student_id=student_id2,Dob=date2,Email=email2,Username=username2,Password=password2)
			db.session.add(entry)
			db.session.commit()
			flash('User successfully registered')
			return render_template('login.html')

# if __name__ == '__main__':
app.run(debug=True)

