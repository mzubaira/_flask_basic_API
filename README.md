## REF
FLASK User Login/Article CRUD: https://www.youtube.com/watch?v=zRwy8gtgJ1A&list=PLcDxVjglvA7lwqZ4WfZyBkE0drLI9yf6U
FLASK Rest API: https://www.youtube.com/watch?v=PTZiDnuC86g&list=PLcDxVjglvA7lwqZ4WfZyBkE0drLI9yf6U&index=7
FLASK ToDo CRUD: https://www.youtube.com/watch?v=oA8brF3w5XQ

## Setting up virtual environment & activating it
pip install pipenv
pipenv shell

# This creates a pipfile

#Installing Flask, SQLAlchemy & Marshmallow
pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
pipenv install requests

# You can check the pipfile:
----------------------------------
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
flask = "*"
flask-sqlalchemy = "*"
flask-marshmallow = "*"
marshmallow-sqlalchemy = "*"

[dev-packages]

[requires]
python_version = "3.11"
----------------------------------

# Marshmallow
object serialization/deserialization library,  converts complex data types to and from Python data types. It is a powerful tool for both validating and converting data.

# jsonify
takes python arrays/dict & convert them in json format

