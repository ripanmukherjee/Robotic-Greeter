#!/bin/ksh

echo "Starting Installing Postgres!!"

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql-client-10 postgresql-10 postgresql-contrib-9.x libpq-dev postgresql-server-dev-10 pgadmin4

echo "Ending Installing Postgres!!"

echo "                                                                                                             "
echo "Installation Done!!"