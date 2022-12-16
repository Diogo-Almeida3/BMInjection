CREATE DATABASE IF NOT EXISTS BMInjection;

USE BMInjection;

CREATE TABLE USERS (
    id          INTEGER         AUTO_INCREMENT,
    username        VARCHAR(255)    NOT NULL,
    email    VARCHAR(255)    NOT NULL UNIQUE,
    pass        VARCHAR(255)    NOT NULL,

    PRIMARY KEY (id)
);