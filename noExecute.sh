#!/usr/bin/env bash
# POSTGRES
#Crear el volumen para no perder dummy datos
docker volume create psql-back
#Instancia y link de base de datos
docker run --name psql -p 5432:5432 --rm -e POSTGRES_PASSWORD=1234 -v psql-back:/var/lib/postgresql/ -d postgres

# MYSQL
docker volume create mysql-back
docker run --name mysql -p 3306:3306 --rm -e MYSQL_ROOT_PASSWORD=4321 -v mysql-back:/var/lib/mysql -d mysql

#Usuarios por defecto en BBDD
#---------------------
#|DB      |  USER
#---------------------
#|psql    |  postgres
#|mysql   |  root