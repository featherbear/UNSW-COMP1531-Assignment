from flask import Flask
app = Flask(__name__, template_folder = '../site/templates', static_folder = '../site/static')

app.run("0.0.0.0", 1313, debug=True)