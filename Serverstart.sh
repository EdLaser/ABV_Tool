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
python3 ./manage.py runserver 141.56.51.110:8000
