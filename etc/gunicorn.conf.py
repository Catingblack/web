

mode = "wsgi"
user = "www-data"
group = "www-data"
daemon = True
pythonpath = "/home/box/web"
wsgi = hello:app
bind = "0.0.0.0:8080"


