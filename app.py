import os
from flask import Flask, render_template, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from model import db, Student, accounts
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/admin-dashboard')
def dashboard():
    total_students = Student.query.count()
    return render_template('dashboard.html', total_students=total_students)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method=='POST'):
        username=request.form['username']
        password=request.form['password']

        user = accounts.query.filter_by(username=username, password=password).first()
        
        if user:
            session['user_id'] = user.user_id
            return redirect (url_for('dashboard'))
        else:
            error_message = "Invalid username or password. Please try again."
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')




@app.route('/users')
def users():
    return render_template('user.html')


@app.route('/audit-trail')
def auditTrail():
    log_entries = Student.query.all()  # Query your database for log entries
    return render_template('auditTrail.html', log_entries=log_entries)


@app.route('/cashout-request')
def cashoutRequest():
    return render_template('cashoutRequest.html')


@app.route('/system-balance')
def systemBalance():
    return render_template('systemBalance.html')


@app.route('/specific-user-transaction')
def specificUserTransaction():
    return render_template('specUserTransaction.html')


@app.route('/specific-user-audit-trail')
def specificUserAuditTrail():
    return render_template('userAuditTrail.html')

@app.route('/user')
def user():
    return render_template('specUser.html')



if __name__ == '__main__':
    app.run(debug=True)
