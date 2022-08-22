#!/bin/bash

#update

sudo apt update
sudo apt install python3.5 -y
sudo apt install python3.5-dev -y
sudo apt install mysql-server-5.6


sudo rm /usr/bin/python3                         
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install gunicorn
sudo pip3 install django==2.1
sudo pip3 install mysqlclient


#config and start nginx and mysql

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

sudo /etc/init.d/mysql start


#set mysql and migrations

mysql -u root -e "create database ask_db"
mysql -u root -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -u root -e  "GRANT ALL PRIVILEGES ON ask_db.* TO 'box'@'localhost' WITH GRANT OPTION;"

python3 /home/box/web/ask/manage.py makemigrations qa
python3 /home/box/web/ask/manage.py migrate



