import os 
import hashlib
import glob
from flask import Flask, flash, request, redirect, url_for
from flask.helpers import send_from_directory
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from werkzeug.utils import secure_filename
from werkzeug.middleware.proxy_fix import ProxyFix
import subprocess 
import zipfile

UPLOAD_FOLDER = '/chal/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["50/hour"]
)

@app.route('/')
def index():
    return '''
    <!doctype html>
    <title>Upload a Cargo project</title>
    <h1>Rust compilation service #2</h1>
    <p>Upload .zip file containing the cargo project to be compiled</p>
    <p>Note: You will be ratelimited to one submission every 5 minutes</p>
    <form method=post action="/upload" enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

def compile_rust(filename):
    try: 
        with zipfile.ZipFile(f"{UPLOAD_FOLDER}/{filename}", 'r') as zip_ref:
            zip_ref.extractall(f"{UPLOAD_FOLDER}/{filename}_dir")
    except:
        return "Invalid zip file"

    # perform macro expansion only, which is what rust analyzer would do in vscode
    # this is all they need to exploit
    cmd = ["cargo", "rustc", "--manifest-path", f"{UPLOAD_FOLDER}/{filename}_dir/Cargo.toml", "--", "-Zunpretty=expanded"]
    try:
        # don't return anything to the user
        proc = subprocess.run(cmd, timeout=300, stdout=subprocess.DEVNULL)
        return "Project successfully added, your project will be reviewed soon"
    except subprocess.TimeoutExpired:
        return "You timed out our poor intern's vscode, what did you do??"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == "zip"

@app.route('/upload', methods=['POST'])
@limiter.limit("1/5minute", override_defaults=False)
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        # filename = secure_filename(file.filename)
        contents = file.read()
        filename = hashlib.md5(contents).hexdigest()
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        with open(path, "wb") as f:
            f.write(contents)

        return compile_rust(filename)
    else:
        return "Wrong file extension: " + file.filename.rsplit('.', 1)[1].lower()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)