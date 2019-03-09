# If database doesn't already exist create it
CREATE DATABASE IF NOT EXISTS datalogger;

# Grant all privileges on datalogger database to pi user
#GRANT ALL PRIVILEGES ON `datalogger`.* TO 'pi'@'localhost' IDENTIFIED BY '';
#GRANT ALL PRIVILEGES ON `datalogger`.* TO pi IDENTIFIED BY '';
#FLUSH PRIVILEGES;

# Switch to datalogger database for table creation and inserts
USE datalogger;

# If config table doesn't already exist create it and insert mandatory config values
CREATE TABLE IF NOT EXISTS `config`(`key` VARCHAR(30) NOT NULL, 
                `value` VARCHAR(30) NOT NULL, 
                `time_created` DATETIME NOT NULL, 
                `time_changed` DATETIME DEFAULT NULL, 
                `active` TINYINT NOT NULL,
CONSTRAINT CONFIG_PK PRIMARY KEY (`active`, 
               `key`)
)ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;
COMMIT;

INSERT INTO `config` VALUES ('AD01', 1, NOW(), '', 1);
INSERT INTO `config` VALUES ('AD02', 1, NOW(), '', 1);
INSERT INTO `config` VALUES ('AD03', 1, NOW(), '', 1);
INSERT INTO `config` VALUES ('AD04', 1, NOW(), '', 1);
INSERT INTO `config` VALUES ('AD05', 0, NOW(), '', 1);
INSERT INTO `config` VALUES ('AD06', 0, NOW(), '', 1);
INSERT INTO `config` VALUES ('AD07', 0, NOW(), '', 1);
INSERT INTO `config` VALUES ('AD08', 0, NOW(), '', 1);
COMMIT;

# If data tables doesn't already exist create it
CREATE TABLE IF NOT EXISTS `data`(`time_created` DATETIME NOT NULL, 
                `key` VARCHAR(30) NOT NULL, 
                `value` DECIMAL(15,6) NOT NULL,
CONSTRAINT DATA_PK PRIMARY KEY(`time_created`, 
               `key`)
)ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4;
COMMIT;

# If tstring tables doesn't already exist create it
CREATE TABLE IF NOT EXISTS `tx_string`(`timestamp` DATETIME NOT NULL, 
                `tx_string` TEXT NOT NULL, 
                `received` TINYINT NOT NULL,
CONSTRAINT CONFIG_PK PRIMARY KEY (`received`, `timestamp`)
)ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 ;
COMMIT;
