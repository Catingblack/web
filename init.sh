#!/bin/bash


if [[ -f /etc/nginx/sites-enabled/default ]]; then
	sudo rm /etc/nginx/sites-enabled/default
	sudo chown -R www-data:www-data /home/box/web
	sudo chmod -R 755 /home/box/web/
	sudo chown -R www-data:www-data /var/log/nginx
	sudo chmod -R 777 /var/log/nginx
fi
	

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo chown -R www-data:www-data /etc/nginx
sudo chmod -R 755 /etc/nginx/
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn_hello.py  /etc/gunicorn.d/gunicorn_hello.py
sudo ln -sf /home/box/web/etc/gunicorn_ask.py  /etc/gunicorn.d/gunicorn_ask.py

sudo gunicorn /etc/init.d/gunicorn restart

sudo gunicorn --config /etc/gunicorn.d/gunicorn_hello.py hello:app && --config /etc/gunicorn.d/gunicorn_ask.py wsgi:application 