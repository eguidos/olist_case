
-- -----------------------------------------------------
-- Table `olist`.`dim_customer`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `olist`.`dim_customer` ;

CREATE TABLE IF NOT EXISTS `olist`.`dim_customer` (
  `customer_id` VARCHAR(100) NOT NULL,
  `customer_unique_id` VARCHAR(100) NULL,
  PRIMARY KEY (`customer_id`))
ENGINE = InnoDB
COMMENT = 'This table contains customer stored data. ';

