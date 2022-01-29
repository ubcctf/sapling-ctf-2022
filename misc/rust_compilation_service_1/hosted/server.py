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
    <h1>Rust compilation service #1</h1>
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

    cmd = ["cargo", "build", "--manifest-path", f"{UPLOAD_FOLDER}/{filename}_dir/Cargo.toml"]
    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    try: 
        proc.wait(timeout=300)
        if proc.returncode != 0:
            error = proc.stderr.read().decode()
            return '''
            <!doctype html>
            <h1> Compilation failed </h1>
            <style>
            pre code {
                background-color: #eee;
                border: 1px solid #999;
                display: block;
                padding: 20px;
            }
            </style>
            <pre>
            <code>''' + error + '''
            </code>
            </pre>
            '''
        else:
            return redirect(f"/results/{filename}")
    except subprocess.TimeoutExpired:
        return "Compilation timed out"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == "zip"

@app.route('/results/<path:filename>')
def download(filename):
    # lmao
    for f in glob.glob(f"{UPLOAD_FOLDER}/{filename}_dir/target/debug/*"):
        f = f.split("/")[-1]
        if f not in [".fingerprint", "build", "deps", "examples", "incremental", ".cargo-lock"]:
            if ".d" not in f:
                binary_name = f 
                break
            
    # i doubt people will try to inject filepaths into their binary names, but even if they do
    # i think this should be safe
    # and meh if they do, they deserve the flag lmao
    return send_from_directory(f"{UPLOAD_FOLDER}/{filename}_dir/target/debug/", binary_name)

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