# These variables will be loaded into the python environment and used by flask to configure your app.
# This may be variables defined by flask, extensions or even your own environment variables.
# This requires that you have the python-dotenv package installed.
# NOTE: This file is placed under version control and should NOT include sensitive information such as passwords.
# For those cases, use the .env file.

FLASK_APP=wsgi:app
FLASK_ENV=development
FLASK_DEBUG=1
