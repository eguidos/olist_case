
-- -----------------------------------------------------
-- Table `olist`.`dim_date`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `olist`.`dim_date` ;

CREATE TABLE IF NOT EXISTS `olist`.`dim_date` (
  `date_id` DATE NOT NULL,
  PRIMARY KEY (`date_id`))
ENGINE = InnoDB
COMMENT = 'This table coontains all stored date values.';