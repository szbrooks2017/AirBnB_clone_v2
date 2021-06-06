-- Create DATABASE - hbnb_dev_db if does not exist
-- Create USER - hbnb_dev (in localhost) if not exist
-- USER password give as 'hbnb_dev_pwd
-- GRANT USER ALL privileges on hbnb_dev_db
-- GRANT USER SELEDT privileges on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL ON hbnb_dev_db.* TO hbnb_dev;

GRANT SELECT ON performance_schema.* TO hbnb_dev;

FLUSH PRIVILEGES;
