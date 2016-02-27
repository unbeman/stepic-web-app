#!/bin/sh
file_path=/home/box/web

sudo rm /etc/nginx/sites-enabled/*
sudo ln  -s $file_path/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
