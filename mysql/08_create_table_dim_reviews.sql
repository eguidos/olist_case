
-- -----------------------------------------------------
-- Table `olist`.`dim_reviews`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `olist`.`dim_reviews` ;

CREATE TABLE IF NOT EXISTS `olist`.`dim_reviews` (
  `review_id` VARCHAR(100) NOT NULL,
  `review_score` VARCHAR(45) NULL,
  `review_comment_title` VARCHAR(45) NULL,
  `review_comment_message` VARCHAR(250) NULL,
  PRIMARY KEY (`review_id`))
ENGINE = InnoDB
COMMENT = 'This table contains reviews sent by customers.';
