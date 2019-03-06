from flask import Flask
app = Flask(__name__, template_folder = '../site/templates', static_folder = '../site/static')

import routes
for module in routes.__modules: app.register_blueprint(routes.__modules[module].site)

app.run("0.0.0.0", 1313, debug=True)