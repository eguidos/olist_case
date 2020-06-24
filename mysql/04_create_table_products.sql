
-- -----------------------------------------------------
-- Table `olist`.`dim_products`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `olist`.`dim_products` ;

CREATE TABLE IF NOT EXISTS `olist`.`dim_products` (
  `product_id` VARCHAR(100) NOT NULL,
  `category_name` VARCHAR(100) NULL,
  `name_lenght` INT NULL,
  `description_lenght` INT NULL,
  `photos_qty` INT NULL,
  `weight_g` INT NULL,
  `length_cm` INT NULL,
  `width_cm` INT NULL,
  PRIMARY KEY (`product_id`))
ENGINE = InnoDB
COMMENT = 'This table contains products stored data.';
