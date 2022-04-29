#!/bin/bash

#bash script to backup the postgres database from the db-docker-container

#get docker container id
containerId = docker ps -aqf "name=^postgres_database$"

#get path where db will stored
path = "./"

#get db name
dnName = "abv"

#lego path incl. filename from multiple strings?
#foo


#get db dump
docker exec -t $containerId  pg_dumpall -c -U $dbName | gzip > dump_$(date +"%Y-%m-%d_%H_%M_%S").gz

#delete dumps that are too old?
#foo