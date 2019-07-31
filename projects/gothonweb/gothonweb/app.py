from flask import Flask, send_from_directory, render_template, request
import os
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def index():
    greeting = 'Hello World'
    return render_template("index.html", greeting=greeting)


@app.route('/this')
def this():
    greeting = 'Hello World'
    return f'Hello, {greeting}!'


@app.route('/that')
def that():
    return send_from_directory(os.path.join(app.root_path, "./templates/"), 'that.html')


# @app.route('/hello')
# def hello():
#     name = request.args.get('name', 'Nobody')

#     if name:
#         greeting = f"Hello {name}"
#     else:
#         greeting = 'Hello World'
#     # http://127.0.0.1:5000/hello?name=Fred sets the name variable to Fred
#     return render_template("index.html", greeting=greeting)

@app.route('/hello')
def hello():
    # name = request.args.get('name', 'Nobody')

    # if name:
    #     greeting = f"Hello {name}"
    # else:
    #     greeting = 'Hello World'
    # http://127.0.0.1:5000/hello?name=Fred sets the name variable to Fred
    return render_template("hello_form.html")


@app.route('/hello', methods=['GET', 'POST'])
def helloso():
    name = request.args.get('name', 'Nobody')

    if request.method == 'POSsT':
        name = request.form['name']
        greet = request.form['greet']
        greeting = f'{greet},{name}'
        return render_template("index.html", greeting=greeting)
    elif request.method == 'GET':
        return render_template("hello_form.html")
    else:
        return f"404 icke funnen 🤯 {dir(app)}"


if __name__ == '__main__':
    app.run()
