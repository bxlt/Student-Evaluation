DROP DATABASE IF EXISTS appDB;
CREATE DATABASE appDB;
USE appDB;

CREATE TABLE Question(
    QuestionID Integer NOT NULL AUTO_INCREMENT,
    Description Varchar(500) NOT NULL,
    Choice Varchar(500) NOT NULL,
    Answer Varchar(500) NOT NULL,
    CONSTRAINT Question_PK PRIMARY KEY(QuestionID)
);
