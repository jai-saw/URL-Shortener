from flask import Flask
from url_shortener.views.main import main

app = Flask(__name__)
app.register_blueprint(main)
