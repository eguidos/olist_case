
-- -----------------------------------------------------
-- Table `olist`.`dim_location`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `olist`.`dim_location` ;

CREATE TABLE IF NOT EXISTS `olist`.`dim_location` (
  `geolocation_zip_code_prefix` INT(11) NOT NULL,
  `geolocation_lat` VARCHAR(45) NULL,
  `geolocation_lng` VARCHAR(45) NULL,
  `geolocation_city` VARCHAR(45) NULL,
  `geolocation_state` VARCHAR(45) NULL,
  PRIMARY KEY (`geolocation_zip_code_prefix`))
ENGINE = InnoDB
COMMENT = 'This table contains data stored location.';
