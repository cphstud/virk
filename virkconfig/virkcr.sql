DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS audits;
DROP TABLE IF EXISTS company;
DROP TABLE IF EXISTS employment;
CREATE TABLE address (
  addressID smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  address varchar(50) NOT NULL,
  address2 varchar(50) DEFAULT NULL,
  city smallint(5) unsigned NOT NULL,
  postal_code varchar(10) DEFAULT NULL,
  phone varchar(20) NOT NULL,
  last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (addressID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE audits (
  auditID smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  cvrnr int(10) unsigned NOT NULL,
  auditYear smallint(5) NOT NULL,
  auditDate Date,
  companyName varchar(150) NOT NULL DEFAULT '',
  companyID smallint(5) NOT NULL,
  GrossResult int(50) DEFAULT NULL,
  Equity int(11) DEFAULT NULL,
  LongTermDebt int(11) DEFAULT NULL,
  SolvencyRatio int(11) DEFAULT NULL,
  AnnualResult int(64) DEFAULT NULL,
  PRIMARY KEY (auditID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE company (
  cvrnr int(10) unsigned NOT NULL,
  companyID smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  companyName varchar(150) NOT NULL DEFAULT '',
  addressID smallint(5) NOT NULL,
  employmentID INT(11) NOT NULL,
  PRIMARY KEY (companyID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE person (
  personID int(10) unsigned NOT NULL AUTO_INCREMENT,
  ssid int(10) unsigned NOT NULL,
  firstname varchar(50) DEFAULT NULL,
  surname varchar(64) DEFAULT NULL,
  fullname varchar(64) DEFAULT NULL,
  role varchar(64) ,
  PRIMARY KEY (personID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
CREATE TABLE employment (
  employmentID int(10) unsigned NOT NULL,
  personID int(10) unsigned NOT NULL,
  companyID int(10) unsigned NOT NULL,
  PRIMARY KEY (employmentID,personID,companyID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
