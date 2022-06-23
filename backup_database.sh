#!/bin/bash

#bash script to backup the postgres database from the db-docker-container
echo "Dies ist ein Script zur Speicherung der Datenbank"
echo "Laufen alle Docker-Container der Antragsverwaltung?"

echo -n "[y|N]"
read -r input1

if [[ $input1 =~ ^[Yy]$ ]]
then
    #get docker container id
    containerId = docker ps -aqf "name=^postgres_database$"

else
    exit

fi

#get path where db will stored
echo -n "Wo soll die Datenbank gespeichert werden?"
read -r path

#get db name
dnName = "abv"

#lego path incl. filename from multiple strings?  ???
$filename=dump_$(date +"%Y-%m-%d_%H_%M_%S").gz
$pathAndFileName="$path$filename"

#get db dump
docker exec -t $containerId  pg_dumpall -c -U $dbName | gzip > dump_$(date +"%Y-%m-%d_%H_%M_%S").gz

#delete dumps that are too old?
#foo