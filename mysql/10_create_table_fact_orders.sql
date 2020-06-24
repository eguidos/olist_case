
-- -----------------------------------------------------
-- Table `olist`.`fact_orders`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `olist`.`fact_orders` ;

CREATE TABLE IF NOT EXISTS `olist`.`fact_orders` (
  `order_id` VARCHAR(100) NOT NULL,
  `customer_id` VARCHAR(100) NOT NULL,
  `order_item_id` VARCHAR(45) NOT NULL,
  `customer_zip_code_prefix` INT(11) NOT NULL,
  `order_status` VARCHAR(45) NULL,
  `order_purchase_date` DATE NOT NULL,
  `order_approved_at` TIMESTAMP NOT NULL,
  `order_delivered_carrier_date` TIMESTAMP NULL,
  `order_delivered_customer_date` TIMESTAMP NULL,
  `order_estimated_delivery_date` TIMESTAMP NULL,
  `payment_type` VARCHAR(45) NULL,
  `payment_installments` INT(11) NULL,
  `payment_value` FLOAT NULL,
  `product_id` VARCHAR(100) NOT NULL,
  `seller_id` VARCHAR(100) NOT NULL,
  `seller_zip_code_prefix` INT(11) NOT NULL,
  `shipping_limit_date` TIMESTAMP NULL,
  `review_id` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`order_id`),
  CONSTRAINT `fk_fact_orders_time1`
    FOREIGN KEY (`order_approved_at`)
    REFERENCES `olist`.`time` (`time_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fact_orders_dim_seller1`
    FOREIGN KEY (`seller_id`)
    REFERENCES `olist`.`dim_seller` (`seller_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fact_orders_dim_products1`
    FOREIGN KEY (`product_id`)
    REFERENCES `olist`.`dim_products` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fact_orders_dim_reviews1`
    FOREIGN KEY (`review_id`)
    REFERENCES `olist`.`dim_reviews` (`review_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fact_orders_dim_location1`
    FOREIGN KEY (`customer_zip_code_prefix`)
    REFERENCES `olist`.`dim_location` (`geolocation_zip_code_prefix`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fact_orders_dim_date1`
    FOREIGN KEY (`order_purchase_date`)
    REFERENCES `olist`.`dim_date` (`date_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fact_orders_dim_items1`
    FOREIGN KEY (`product_id`)
    REFERENCES `olist`.`dim_items` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fact_orders_dim_customer101`
    FOREIGN KEY (`customer_id`)
    REFERENCES `olist`.`dim_customer` (`customer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_fact_orders_dim_location31`
    FOREIGN KEY (`seller_zip_code_prefix`)
    REFERENCES `olist`.`dim_location` (`geolocation_zip_code_prefix`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
COMMENT = 'This table contains salles stored data, in order to create layers for data analysis.';
