from flask import Flask,render_template,request,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import forms,os
import models
from werkzeug.utils import secure_filename
#app = Flask(__name__)
ALLOWED_EXTENSION=set(['pdf','exe','zip','gz','deb'])

app = Flask(__name__)
#database configuration
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
app.config['UPLOAD_FOLDER']='C:/Users/srina/PycharmProjects/softstack/static'
#app.config['UPLOADED_FILES_ALLOW']= 'exe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/srina/PycharmProjects/thumbs.db'
app.config['DEBUG'] = True
db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/',methods=["POST","GET"])
def main_page():
    stack = models.Software.query.order_by(desc(models.Software.upload_time)).limit(10)
    if request.method == 'GET':
        query = request.args.get(key='search_bar', default='')
        see = "%{0}%".format(query)
        if query != '':
            stack = models.Software.query.filter(
                models.Software.name.ilike(see) | models.Software.description.ilike(see)).limit(10)
    return render_template("template.html",stack=stack,query=query)


@app.route('/upload',methods=["POST","GET"])
def upload_page():
    form=forms.UploadForm()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'software' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['software']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            name=file.filename

        if form.validate_on_submit() and models.Software.query.filter_by(name=name):
            description=form.description.data
            userid=form.username.data
            password=form.password.data
            if models.User.query.filter_by(username=userid).first().password==password:
                record=models.Software(name=name,userid=userid,description=description)
                db.session.add(record)
                db.session.commit()
            return redirect(url_for('main_page'))
        else:
            flash('record already exists or form not filled properly')
    return render_template("upload_form.html",form=form)

@app.route('/terms')
def term_page():
    return render_template("terms.html")

@app.route('/simple')
def simple_page():
    stack = models.Software.query.order_by(desc(models.Software.upload_time)).limit(10)
    if request.method == 'GET':
        query = request.args.get(key='search_bar', default='')
        see = "%{0}%".format(query)
        if query != '':
            stack = models.Software.query.filter(
                models.Software.name.ilike(see) | models.Software.description.ilike(see)).limit(10)
    return render_template("simple.html",stack=stack)

@app.route('/signup',methods=["GET","POST"])
def signup_page():
    form=forms.RegisterForm()
    if form.validate_on_submit():
        roll=form.roll.data
        username=form.username.data
        password=form.password.data
        with open('C:/Users/srina/PycharmProjects/softstack/user_request.csv','a') as f:
            f.seek(2)
            f.write("{0},{1},{2}\n".format(roll,username,password))
            flash('request submitted ! u can check back in a week.')
    return render_template('signup.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
