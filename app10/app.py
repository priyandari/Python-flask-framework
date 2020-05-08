from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = os.path.realpath('.') + \
    '\\app10\\static\\uploads'
application.config['MAX_CONTENT_PATH'] = 100000000

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        filename = application.config['UPLOAD_FOLDER'] + \
            '\\' + secure_filename(f.filename)
        try:
            f.save(filename)
            return render_template('upload_sukses.html', filename=secure_filename(f.filename))
        except:
            return render_template('upload_gagal.html', filename=secure_filename(f.filename))
    return render_template('form.html')

if __name__=='__main__':
    application.run(debug=True)
