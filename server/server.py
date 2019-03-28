from flask import Flask
app = Flask(__name__, template_folder = '../site/templates', static_folder = '../site/assets', static_url_path='/assets')

from lib import database
database.init()

import routes
for module in routes.__modules: app.register_blueprint(routes.__modules[module].site)

from GourmetBurgers.sql_table_definitions import data as sql_table_definitions

for value in sql_table_definitions.values():
    database.create_table(value)

app.run("0.0.0.0", 1313, debug=True)