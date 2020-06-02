Install Postgres SQL on Ubuntu 18.04
------------------------------------------------
PostgreSQL is available in all Ubuntu versions by default. However, Ubuntu "snapshots" a specific
version of PostgreSQL that is then supported throughout the lifetime of that Ubuntu version.
Other versions of PostgreSQL are available through the PostgreSQL apt repository.

Prerequisites
--------------
* A system running Ubuntu 18.04
* A user account with sudo privileges
* Access to a terminal window/command-line (Ctrl+Alt+T)

Before continuing with this tutorial, make sure you are logged in as root or a user with sudo
privileges.

Check your version of pip by entering the following::

    $ pip ––version

There are 2 way you can install the packages:

1. Install using Command Prompt.
2. Install via shell scripts.

1. Install using Command Prompt:
*********************************
First, we need to update and upgrade it::

    $ sudo apt update

    $ sudo apt upgrade

Then we need to install postgres module as follow::

    $ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ bionic-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'

    $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

    $ sudo apt-get update

    $ sudo apt-get install postgresql-client-10 postgresql-10 postgresql-contrib-9.x libpq-dev postgresql-server-dev-10 pgadmin4


2. Install via shell scripts:
*********************************
On the other hand you can run the shell script PostgreSQL_pgAdmin_Installation.sh_ in the
PostgreSQL_pgAdmin_Installation folder. By running this program, it will automatically install
postgres and pgAdmin4 for you.

.. _PostgreSQL_pgAdmin_Installation.sh:

You can run the shell script as follow::

    $ chmod +x *.sh

    $ sh PostgreSQL_pgAdmin_Installation.sh

Installation done!!

Please visit the PostgreSQL_ website for how to install postgres related details.

.. _PostgreSQL: https://www.postgresql.org/download/linux/ubuntu/

3. Working with postgreSQL:
***********************************
After you are done installing postgreSQL, go to your command prompt and check postgresSQL as follow::

    $ sudo -u postgres psql postgres

The default username and password for postgreSQL is postgres. Also, you can change the password as follow ::

    postgres=# alter user postgres with password 'example_password';

Also, you can check the database present in your postgreSQL as follow::

    postgres=# \l

    Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
    -----------+----------+----------+-------------+-------------+-----------------------
    postgres  | postgres | UTF8     | en_CA.UTF-8 | en_CA.UTF-8 |
    template0 | postgres | UTF8     | en_CA.UTF-8 | en_CA.UTF-8 | =c/postgres          +
    |          |          |             |             | postgres=CTc/postgres
    template1 | postgres | UTF8     | en_CA.UTF-8 | en_CA.UTF-8 | =c/postgres          +
    |          |          |             |             | postgres=CTc/postgres

If you want to create new database then do as follow::

    postgres=# create database caregodb;
    CREATE DATABASE
    postgres=# \l
                                             List of databases
       Name    |  Owner   | Encoding |      Collate       |       Ctype        |   Access privileges
    -----------+----------+----------+--------------------+--------------------+-----------------------
    caregodb  | postgres | UTF8     | en_CA.UTF-8 | en_CA.UTF-8 |
    postgres  | postgres | UTF8     | en_CA.UTF-8 | en_CA.UTF-8 |
    template0 | postgres | UTF8     | en_CA.UTF-8 | en_CA.UTF-8 | =c/postgres          +
    |          |          |             |             | postgres=CTc/postgres
    template1 | postgres | UTF8     | en_CA.UTF-8 | en_CA.UTF-8 | =c/postgres          +
    |          |          |             |             | postgres=CTc/postgres
        (4 rows)

If you need to enter into particular database then do as follow::

    postgres=# \c caregodb
    psql (12.3 (Ubuntu 12.3-1.pgdg18.04+1), server 11.8 (Ubuntu 11.8-1.pgdg18.04+1))
    You are now connected to database "caregodb" as user "postgres".
    caregodb=#


if you need to check how many table present in current database then do as follow ::

    caregodb=# \d
                         List of relations
     Schema |            Name            |   Type   |  Owner
    --------+----------------------------+----------+----------
     public | carego_customer_dev        | table    | postgres
     public | carego_customer_dev_ID_seq | sequence | postgres
    (2 rows)


4. Working with pgAdmin4:
***********************************
If you performed the above mentioned steps then you should have pgAdmin4 installed in your computer. Now search
pgAdmin4 in your computer (Windows : Start Menu, ubuntu : Activities) and open it.

* Once you open pgAdmin4, it will ask for the password. Please type your system password.
* It will open one web browser for you. There you need to click on server.
* Again it will ask for password, now type password for postgres (default password - postgres)
* Here you can see your earlier created caregodb database.

5. Working with caregodb Database:
**************************************
In this part we will create the table, create unique key and insert the data. Please go to pgAdmin_Document
for more details regarding the same.
