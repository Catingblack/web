#!/bin/bash


if [[ -f /etc/nginx/sites-enabled/default ]]; then
	sudo rm /etc/nginx/sites-enabled/default
	sudo chown -R www-data:www-data /home/box/web
	sudo chmod -R 755 /home/box/web/
fi
	

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo chown -R www-data:www-data /etc/nginx
sudo chmod -R 755 /etc/nginx/
sudo /etc/init.d/nginx restart

	
sudo ln -sf /home/box/web/etc/gunicorn.conf.py   /etc/gunicorn.d/test
sudo chown -R www-data:www-data /etc/gunicorn.d
sudo chmod -R 755 /etc/gunicorn.d/
sudo /etc/init.d/gunicorn restart