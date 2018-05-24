
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello Linux World"


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


if __name__ == '__main__':
    app.run(debug = True)

