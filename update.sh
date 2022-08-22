sudo apt update
sudo apt install python3.5 -y
sudo apt install python3.5-dev -y


sudo rm /usr/bin/python3                         
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install gunicorn
sudo pip3 install django==2.1
sudo pip3 install mysqlclient
