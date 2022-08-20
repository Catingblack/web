sudo apt update
sudo pip install python3.5

virtualenv -p "/usr/bin/python3.5" env
source env/bin/activate
pip install gunicorn django==2.0