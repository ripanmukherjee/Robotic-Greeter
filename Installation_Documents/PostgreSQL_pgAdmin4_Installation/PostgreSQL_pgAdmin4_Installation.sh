#!/bin/ksh

echo "                                             "
echo "Starting Installation PostgreSQL and pgAdmin4!!"
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update

echo "                                           "
echo "Starting Installation -- postgresql-client-10"
sudo apt-get install postgresql-client-10

echo "                                          "
echo "Starting Installation -- postgresql-10"
sudo apt-get install postgresql-10

echo "                                         "
echo "Starting Installation -- postgresql-contrib"
sudo apt-get install postgresql-contrib

echo "                                "
echo "Starting Installation -- libpq-dev"
sudo apt-get install libpq-dev

echo "                                               "
echo "Starting Installation -- postgresql-server-dev-10"
sudo apt-get install postgresql-server-dev-10

echo "                               "
echo "Starting Installation -- pgadmin4"
sudo apt-get install pgadmin4

echo "                               "
echo "Starting Installation -- psycopg2"
sudo apt-get install -y python3-psycopg2
echo "Ending Installation PostgreSQL and pgAdmin4!!"

echo "                   "
echo "Installation Done!!"