from flask import Flask
app = Flask(__name__, template_folder = '../site/templates', static_folder = '../site/assets', static_url_path='/assets')

import routes
for module in routes.__modules: app.register_blueprint(routes.__modules[module].site)

from lib import database
from lib.tableQueries import SQL

for value in SQL.values():
    database.create_table(value)

app.run("0.0.0.0", 1313, debug=False)