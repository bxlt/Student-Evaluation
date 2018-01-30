USE appDB;

CREATE TABLE Assignment(
    AssignmentID Integer NOT NULL AUTO_INCREMENT,
    Name VARCHAR(100) NOT NULL,
    CONSTRAINT Assignment_PK PRIMARY KEY(AssignmentID)
);

CREATE TABLE AssignmentQuestions(
    AssignmentID INTEGER NOT NULL,
    ProblemID INTEGER NOT NULL,
    PRIMARY KEY (AssignmentID, ProblemID)
);