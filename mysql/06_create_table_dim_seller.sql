
-- -----------------------------------------------------
-- Table `olist`.`dim_seller`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `olist`.`dim_seller` ;

CREATE TABLE IF NOT EXISTS `olist`.`dim_seller` (
  `seller_id` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`seller_id`))
ENGINE = InnoDB
COMMENT = 'This table contains sellers stored data.';
