
-- -----------------------------------------------------
-- Table `olist`.`dim_items`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `olist`.`dim_items` ;

CREATE TABLE IF NOT EXISTS `olist`.`dim_items` (
  `product_id` VARCHAR(100) NOT NULL,
  `price` VARCHAR(45) NULL,
  `freight_value` VARCHAR(45) NULL,
  PRIMARY KEY (`product_id`))
ENGINE = InnoDB
COMMENT = 'This table contains items stored data.';

DESCRIBE `olist`.`dim_items`;