#!/usr/bin/env bash

mysql --user=root --password="$MYSQL_ROOT_PASSWORD" <<-EOSQL
    CREATE DATABASE IF NOT EXISTS hackme_db;
    CREATE USER IF NOT EXISTS 'hack'@'%' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON \`hackme_db%\`.* TO 'hack'@'%';
EOSQL
