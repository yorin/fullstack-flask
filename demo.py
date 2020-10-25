from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__,static_url_path="", static_folder="static")
app.secretkey = 'jumpjacks'

username = ' '
user = model.check_users('username')


@app.route('/', methods = ['GET'])
def home():
    
        return render_template ('index.html')
    
@app.route('/about', methods = ['GET'])
def about():
    return render_template ('about.html')

@app.route('/terms-of-use', methods = ['GET'])
def terms():
    return render_template ('terms.html')

@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template ('privacy.html')

@app.route('/portal', methods = ['GET', 'POST'])
def portal():
    if 'username' in session:
        g.user=session['username']
        return render_template ('portal.html')
    return render_template ('login.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    #if request.method == "GET":
    #    return render_template ('login.html')
    if request.method == "POST":
        session.pop("username", None)
        areyouser = request.form['username']
        pwd = model.check_pw(areyouser)
        dump(obj)
        if request.form['password'] == pwd:
            session = ['username'] == request.form['username']
            return redirect(url_for('portal'))
    return render_template('login.html')
"""    else:
        Username = request.form['username']
        Password = request.form['password']
        #print ('username:', Username, file=sys.stderr)
        #print ('password:', Password, file=sys.stderr)        
        db_passwd = model.check_pw(Username)
        if Username is None:
           error_message = 'your username & password is incorrect.'
           return render_template('login.html', message = error_message)
        if Password is None:
           error_message = 'your username & password is incorrect.'
           return render_template('login.html', message = error_message) 
        if Password == db_passwd:
            #message = model.show_color('GORDON')
            message = model.fetch_all(Username)
            return render_template('portal.html', message = message)
        else:
            error_message = 'your username & password is incorrect.'
            return render_template('login.html', message = error_message) """

@app.before_request
def before_request():
    g.username = None
    if username in session:
        g.username = session['username']

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))    

app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/signup', methods = ['GET','POST'])
def signup():
    if request.method == "GET":
        message ='Please Sign-up'
        return render_template ('signup.html', message = message)
    else:    
        Username = request.form['username']
        Password = request.form['password']
        message  = model.signup(Username, Password)
        return render_template ('signup.html', message= message) 


if __name__=='__main__':
    app.run(port = 7000, debug= True)
