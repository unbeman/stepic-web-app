#!/usr/bin/env bash

sudo rm /etc/nginx/sites-enabled/default

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart

sudo /etc/init.d/mysql restart

mysql -uroot -e "create user 'django'@'localhost' identified by 'django';"
mysql -uroot -e "grant all privileges on * . * to 'django'@'localhost';"
mysql -uroot -e "flush privileges;"
