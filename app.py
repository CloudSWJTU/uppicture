from flask import Flask, render_template, request,url_for
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploadsofpicture'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:pxt20020918@127.0.0.1/try1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True
db = SQLAlchemy(app)

class picture(db.Model):
    __tablename__ = 'pictureofhistory'
    idofpicture = db.Column(db.Integer,primary_key=True)
    userid = db.Column(db.Integer, unique=True)
    picturename=db.Column(db.String(80),unique=True)
    username= db.Column(db.String(80), unique=True)
    uploadtime=db.Column(db.Integer,unique=True)
    status= db.Column(db.String(80), unique=False)#管理员设置状态

@app.route('/')
def index():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    image_urls = [f"/static/uploadsofpicture/{img}" for img in images if img.endswith(('jpg', 'jpeg', 'png', 'gif'))]
    return render_template('indexp.html', image_urls=image_urls)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        getpicturename=request.files.get('picturename')
        #获取图片地址，名字，以及用户的名字，id，图片id由随机数生成（如何不重复）
        thep=picture(picturename= getpicturename)
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return index()

if __name__ == '__main__':
    app.run(debug=True)
