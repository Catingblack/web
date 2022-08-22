#!/bin/bash


if [[ -f /etc/nginx/sites-enabled/default ]]; then
	sudo rm /etc/nginx/sites-enabled/default
	sudo chown -R www-data:www-data /home/box/web
	sudo chmod -R 777 /home/box/web/
	sudo chown -R www-data:www-data /var/log/nginx
	sudo chmod -R 777 /var/log/nginx
fi
	

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo chown -R www-data:www-data /etc/nginx
sudo chmod -R 755 /etc/nginx/
sudo /etc/init.d/nginx restart

