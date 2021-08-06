#!/bin/bash

clear
echo "Check for new migrations"
python3 ./manage.py makemigrations
echo "Done"
echo "------------------------------------------------"
echo "Waiting"
sleep 5s
echo "Start migration process"
python3 ./manage.py migrate
echo "Done"
echo "------------------------------------------------"
echo "Waiting"
sleep 5s
clear
echo "Startig Server"
python3 ./manage.py runserver 0.0.0.0:8000
