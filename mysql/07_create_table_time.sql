
-- -----------------------------------------------------
-- Table `olist`.`time`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `olist`.`time` ;

CREATE TABLE IF NOT EXISTS `olist`.`time` (
  `time_id` TIMESTAMP NOT NULL,
  PRIMARY KEY (`time_id`))
ENGINE = InnoDB
COMMENT = 'This table contains time stored data.';