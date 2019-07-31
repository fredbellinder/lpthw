from gothonweb import yolo
from flask import Flask, send_from_directory
import os
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/')
def hello_world(yolo=yolo):
    return yolo
    # send_from_directory(os.path.join(app.root_path), 'index2.html')


if __name__ == '__main__':
    app.run()
