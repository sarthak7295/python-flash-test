
import os
from flask import Flask, request, render_template,redirect, url_for
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '/home/sarthak/FlaskPics'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def hello_world():
    return render_template('upl.html')


@app.route('/hello')
def hello_world2():
    return 'hello world2'


@app.route('/hello/<value>')
def variable_test(value):
    return 'hello world '+value


@app.route('/hellonumber/<int:post_id>')
def show_blog(post_id):
    return 'Blog Number %d' % post_id


@app.route('/helloheading')
def index():
    return render_template('hello.html', name='sarthak')

@app.route('/save', methods=['GET', 'POST'])
def save_image():
    data = request.data
    print(data)
    return render_template('hello.html', name='sarthak')



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'done upload'#redirect(url_for('uploaded_file',filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug='true',host='0.0.0.0' ,port=8080)

