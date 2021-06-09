-- Create DATABASE - hbnb_dev_db if does not exist
-- Create USER - hbnb_dev (in localhost) if not exist
-- USER password give as 'hbnb_dev_pwd
-- GRANT USER ALL privileges on hbnb_dev_db
-- GRANT USER SELEDT privileges on performance_schema

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

USE hbnb_dev_db;

DROP USER IF EXISTS 'hbnb_dev'@'localhost';

CREATE USER 'hbnb_dev'@'localhost';

SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
