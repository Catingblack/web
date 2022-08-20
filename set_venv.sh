
virtualenv -p "/usr/bin/python3.5" env 2 > /dev/null
source env/bin/activate
pip install gunicorn django==2.

