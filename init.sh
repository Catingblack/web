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

sudo /etc/init.d/mysql start

mysql -u root -e "create database ask_db"
mysql -u root -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -u root -e  "GRANT ALL PRIVILEGES ON ask_db.* TO 'box'@'localhost' WITH GRANT OPTION;"

./manage.py makemigrations
./manage.py migrate
