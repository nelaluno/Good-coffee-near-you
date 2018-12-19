SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
CREATE TABLE IF NOT EXISTS `CoffeeHouses`.`address` (
  `address_id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(250) NULL,
  `coffee_house_id` VARCHAR(100) NOT NULL,
  `latitude` INT NULL,
  `longitude` INT NULL,
  PRIMARY KEY (`address_id`),
  UNIQUE INDEX `address_id_UNIQUE` (`address_id` ASC),
  INDEX `coffee_house_id_idx` (`coffee_house_id` ASC),
  CONSTRAINT `coffee_house_id`
    FOREIGN KEY (`coffee_house_id`)
    REFERENCES `mydb`.`Coffee_house` (`idCoffee_house_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `CoffeeHouses`.`Coffee_house` (
  `idCoffee_house_id` VARCHAR(100) NOT NULL,
  `name` VARCHAR(100) NULL,
  `adress_id` INT NULL,
  `Has_food_to_go` TINYINT(1) NULL,
  PRIMARY KEY (`idCoffee_house_id`),
  UNIQUE INDEX `idCoffee_house_id_UNIQUE` (`idCoffee_house_id` ASC),
  INDEX `address_id_idx` (`adress_id` ASC),
  CONSTRAINT `address_id`
    FOREIGN KEY (`adress_id`)
    REFERENCES `mydb`.`address` (`address_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `CoffeeHouses`.`working_time` (
  `day_of_week` INT NOT NULL AUTO_INCREMENT,
  `opening_hours` TIME NULL,
  `closing_hours` TIME NULL,
  `coffee_house_id` VARCHAR(100) NULL,
  PRIMARY KEY (`day_of_week`),
  UNIQUE INDEX `day_of_week_UNIQUE` (`day_of_week` ASC),
  INDEX `coffee_house_id_idx` (`coffee_house_id` ASC),
  CONSTRAINT `coffee_house_id`
    FOREIGN KEY (`coffee_house_id`)
    REFERENCES `mydb`.`Coffee_house` (`idCoffee_house_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `CoffeeHouses`.`form_new_place` (
  `coffe_house_name` VARCHAR(100) NOT NULL,
  `phone_number` INT UNSIGNED NULL,
  `web_site` VARCHAR(2083) NULL,
  `latte_cost` FLOAT NULL,
  `cappuccino_cost` FLOAT NULL,
  `americano_cost` FLOAT NULL,
  `address` VARCHAR(250) NULL,
  `latitude` INT NULL,
  `longtitude` INT NULL,
  `hours` TIME NULL,
  `HasFoodToGo` TINYINT(1) NULL,
  PRIMARY KEY (`coffe_house_name`),
  UNIQUE INDEX `coffe_house_name_UNIQUE` (`coffe_house_name` ASC))
ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `CoffeeHouses`.`total_rating` (
  `coffee_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `total_rating` FLOAT UNSIGNED NULL,
  `rating_count` INT UNSIGNED NULL,
  `coffee_house_id` VARCHAR(100) NULL,
  PRIMARY KEY (`coffee_id`),
  UNIQUE INDEX `coffee_id_UNIQUE` (`coffee_id` ASC),
  INDEX `coffee_house_id_idx` (`coffee_house_id` ASC),
  CONSTRAINT `coffee_house_id`
    FOREIGN KEY (`coffee_house_id`)
    REFERENCES `mydb`.`Coffee_house` (`idCoffee_house_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `CoffeeHouses`.`form_new_price` (
  `coffee_house_name` VARCHAR(100) NOT NULL,
  `phone_number` INT UNSIGNED NULL,
  `website` VARCHAR(2083) NULL,
  `latte_cost` FLOAT NULL,
  `cappuccino_cost` FLOAT NULL,
  `americano_cost` FLOAT NULL,
  PRIMARY KEY (`coffee_house_name`),
  UNIQUE INDEX `coffee_house_name_UNIQUE` (`coffee_house_name` ASC))
ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `CoffeeHouses`.`price` (
  `coffee_id` INT NOT NULL AUTO_INCREMENT,
  `cost` FLOAT NULL,
  `coffee_house_id` VARCHAR(100) NULL,
  PRIMARY KEY (`coffee_id`),
  UNIQUE INDEX `coffee_id_UNIQUE` (`coffee_id` ASC),
  INDEX `coffee_house_id_idx` (`coffee_house_id` ASC),
  CONSTRAINT `coffee_house_id`
    FOREIGN KEY (`coffee_house_id`)
    REFERENCES `mydb`.`Coffee_house` (`idCoffee_house_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS `CoffeeHouses`.`user_rating` (
  `user_id` INT NULL,
  `user_rating` FLOAT NULL,
  `coffee_house_id` VARCHAR(100) NULL,
  `coffee_id` INT NULL,
  INDEX `coffee_house_id_idx` (`coffee_house_id` ASC),
  CONSTRAINT `coffee_house_id`
    FOREIGN KEY (`coffee_house_id`)
    REFERENCES `mydb`.`Coffee_house` (`idCoffee_house_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;