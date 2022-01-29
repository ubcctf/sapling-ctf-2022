from flask import Flask, request, render_template
app = Flask(__name__)

directories = ['resources']
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/oot')
def owo():
    f = request.args.get('oot')
    f = f + '.txt'
    directories.append(f)
    filename = '/'.join(directories)
    try:
        with open(filename, 'r') as filename:
            file_content = filename.read(-1)
    except:
        file_content = "INVALID FACT"
    finally:
        directories.pop()
    return render_template("portfolio.html", oot=file_content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5000)