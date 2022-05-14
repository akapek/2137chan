from flask import Flask, redirect, url_for, render_template, request, send_from_directory
import requests
import os

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')
@app.route("/")
def home():
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True, port=2137)
