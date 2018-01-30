USE appDB;

CREATE TABLE StudentAnswer(
    QuestionID INTEGER NOT NULL,
    StudentID INTEGER NOT NULL,
    Answer VARCHAR(500) NOT NULL,
    PRIMARY KEY (QuestionID,StudentID)
);