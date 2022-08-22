sudo apt update
sudo apt install python3.5
sudo apt install mysql-server-5.6

sudo rm /usr/bin/python3                         
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install gunicorn
sudo pip3 install django==2.1
