from flask import Flask, request
import sqlite as dbapi
con = dbapi.connect('number.db')
cur= con.cursor()
app = Flask(__name__)
cur.execute('UPDATE NUMBERUD SET Number = 0')
con.commit()



@app.route('/add')
def plus():
	cur.execute('SELECT Number FROM NUMBERUD')
	a = cur.fetchone()[0]+1
	cur.execute('UPDATE NUMBERUD SET Number = %d'%a)
	con.commit()
	return '%d' %a

@app.route('/subtract')
def minus():
	cur.execute('SELECT Number FROM NUMBERUD')
	a = cur.fetchone()[0]-1
	cur.execute('UPDATE NUMBERUD SET Number = %d'%a)
	con.commit()
	return '%d' %a

@app.route('/',methods=['GET','POST'])
def hello():
	cur.execute('SELECT Number FROM NUMBERUD')
	a = cur.fetchone()[0]
	return '%d' %a

@app.route('/sub')
def sub():
	return "ddd"

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'post %d' % post_id



@app.route('/login',methods=['GET','POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()

if __name__ == "__main__":
	app.run(host='0.0.0.0')
