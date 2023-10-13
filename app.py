from flask import Flask, render_template

app = Flask(__name__)   

@app.route('/admin-dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/users')
def users():
    return render_template('user.html')


@app.route('/audit-trail')
def auditTrail():
    return render_template('auditTrail.html')


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
