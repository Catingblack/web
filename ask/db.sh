
sudo /etc/init.d/mysql start

mysql -u root -e "create database ask_db"
mysql -u root -e "CREATE USER 'box'@'localhost' IDENTIFIED BY '1234';"
mysql -u root -e  "GRANT ALL PRIVILEGES ON ask_db.* TO 'box'@'localhost' WITH GRANT OPTION;"

python3 manage.py makemigrations qa
python3 manage.py migrate
