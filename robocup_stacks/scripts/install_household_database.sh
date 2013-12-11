#!/bin/bash
# Automating https://docs.google.com/document/d/1i1rm06VAqlks_aEX5AmyL9Usx7FTwEOBF9vxKmqyd2Q/edit

# from http://serverfault.com/questions/44400/run-a-shell-script-as-a-different-user
# psql --help

#### I SUPPOSE THIS IS EXECUTED FROM /mnt_flash/robocup2013/reem_at_iri/trunk/scripts !!

# SET VARIABLES!
WHERE_TO_STORE_PLYS="/mnt_flash/robocup2013/household_plys"
# if it doesnt exist:
mkdir -p /mnt_flash/robocup2013/household_plys

#WHERE_TO_STORE_PLYS="/home/r0s/household_plys"
PATH_TO_BACKUP_OBJECTS_DB=$(rospack find scripts)
#PATH_TO_BACKUP_OBJECTS_DB="/mnt_flash/robocup2013/reem_at_iri/scripts"
#PATH_TO_BACKUP_OBJECTS_DB="/home/r0s/robocup2013/reem_at_iri/trunk/scripts"


# if we need to drop user for testing:
# sudo su - postgres -c "psql -c \"DROP USER willow \";"
echo "--- Creating willow willow User and Pass"
# in the robot I need to delete the "sudo"
su - postgres -c "psql -c \"CREATE ROLE willow LOGIN CREATEDB CREATEROLE PASSWORD 'willow';\""

# if we need to add it by hand for testing:
#sudo sh -c "echo \"# Anybody through TCP/IP with password
#host    all         all         0.0.0.0   0.0.0.0     md5\" >> /etc/postgresql/9.1/main/pg_hba.conf"
# sudo sh -c "echo \"listen_addresses = '*'\" >> /etc/postgresql/9.1/main/postgresql.conf"

echo "--- Setting config files"
echo "# Anybody through TCP/IP with password
host    all         all         0.0.0.0   0.0.0.0     md5" >> /etc/postgresql/9.1/main/pg_hba.conf
# echo  "# "local" is for Unix domain socket connections only
# local   all		 all							   trust"  >> /etc/postgresql/9.1/main/pg_hba.conf
echo "listen_addresses = '*'" >> /etc/postgresql/9.1/main/postgresql.conf

# Now we need to restore our database with the backup file

#NOW ITS DIRECTLY COMPRESSED ON THE FILE
# echo "--- Extracting from database backup"
# tar -zxvf backup_objects_db/household_objects_db_backup.tar.gz
# mv *.backup backup_objects_db
# echo "--- Creating database household_objects"


# Query obtained from pgadmin3 creating a new db with the GUI and choosing the DB
su - postgres -c "psql -c \"
CREATE DATABASE household_objects
  WITH OWNER = willow
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_GB.UTF-8'
       LC_CTYPE = 'en_GB.UTF-8'
       CONNECTION LIMIT = -1;\""

#echo "--- Setting up PGPASSWORD"
# this shit doesnt work at all
# su - postgres -c "export PGPASSFILE=\"'$PATH_TO_BACKUP_OBJECTS_DB'/.pgpass.conf\""
# echo "--- Write to .pgpass.conf"
# echo "localhost:5432:household_objects:willow:willow" > '$PATH_TO_BACKUP_OBJECTS_DB'/.pgpass.conf
# chmod 0600 '$PATH_TO_BACKUP_OBJECTS_DB'/.pgpass.conf

#su - postgres -c "export PGPASSWORD=willow"
# This last line should work with the --no-passowrd parameter in the next command.. but it doesnt
echo "--- Restoring backup"
echo "Please enter the password: willow"
su - postgres -c 'pg_restore --host localhost --port 5432 --username "willow" --dbname "household_objects" --role "willow" --verbose "'$PATH_TO_BACKUP_OBJECTS_DB'/backup_objects_db/household_ROBOCUP.backup"'
#echo "--- Deleting intermediate files"
#rm backup_objects_db/*.backup

# Now we need to modify the Table "variable" 
# Key: MODEL_ROOT 2 /mnt_flash/robocup/household_plys
# And that URL should exist
echo "--- Setting up URL for plys of trained objects"
su - postgres -c "psql --dbname=household_objects -c \"UPDATE variable SET variable_value = '$WHERE_TO_STORE_PLYS' WHERE variable_name = 'MODEL_ROOT';\""

echo "--- Restarting postgresql to be able to access from outside of the robot"
/etc/init.d/postgresql restart
