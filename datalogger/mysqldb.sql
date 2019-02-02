CREATE DATABASE IF NOT EXISTS datalogger;

#CREATE USER IF NOT EXISTS 'pi'@'localhost' IDENTIFIED BY '';
#GRANT ALL PRIVILEGES ON `datalogger`.* TO 'pi'@'localhost';
#FLUSH PRIVILEGES;
USE datalogger;

CREATE TABLE config(`key` VARCHAR(30) NOT NULL, 
                `value` VARCHAR(30) NOT NULL, 
                `time_created` DATETIME NOT NULL, 
                `time_changed` DATETIME DEFAULT NULL, 
                `active` TINYINT NOT NULL,
CONSTRAINT CONFIG_PK PRIMARY KEY (`active`, 
               `key`)
)ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;
COMMIT;

CREATE TABLE data(`time_created` DATETIME NOT NULL, 
                `key` VARCHAR(20) NOT NULL, 
                `value` DECIMAL(15,4) NOT NULL,
CONSTRAINT DATA_PK PRIMARY KEY(`time_created`, 
               `key`)
)ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;
COMMIT;

CREATE TABLE tstring(`tstring` TEXT NOT NULL, 
                `received` TINYINT NOT NULL,
CONSTRAINT CONFIG_PK PRIMARY KEY (`received`)
)ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 ;
COMMIT;
