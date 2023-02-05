-- Create tables

CREATE TABLE Customers (
    customerID int NOT NULL AUTO_INCREMENT,
    customerName varchar(50) NOT NULL,
    altName varchar(50) NULL,
    phone varchar(20) NOT NULL,
    email varchar(50),
    PRIMARY KEY (customerID)
);

CREATE TABLE Dogs (
    dogID int NOT NULL AUTO_INCREMENT,
    customerID int NOT NULL,
    dogName varchar(50) NOT NULL,
    dogBirthday date NOT NULL,
    active boolean,
    PRIMARY KEY (dogID),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID) ON DELETE CASCADE
);

CREATE TABLE Employees (
    employeeID int NOT NULL AUTO_INCREMENT,
    employeeName varchar(50) NOT NULL,
    employeeType varchar(50) NOT NULL,
    PRIMARY KEY (employeeID)
);

CREATE TABLE Commands (
    commandID int NOT NULL AUTO_INCREMENT,
    commandName varchar(50) NOT NULL,
    PRIMARY KEY (commandID)
);

CREATE TABLE TrainingSessions (
    sessionID int NOT NULL AUTO_INCREMENT,
    customerID int NOT NULL,
    dogID int NOT NULL,
    employeeID int NOT NULL,
    sessionDate date NOT NULL,
    notes varchar(300) NOT NULL,
    PRIMARY KEY (sessionID),
    FOREIGN KEY (customerID) REFERENCES Customers(customerID),
    FOREIGN KEY (dogID) REFERENCES Dogs(dogID),
    FOREIGN KEY (employeeID) REFERENCES Employees(employeeID)
    ON DELETE CASCADE
);

CREATE TABLE CommandsLearned (
  commandsLearnedByDog varchar(50),
  commandID int NOT NULL,
  dogID int NOT NULL,
  PRIMARY KEY (commandsLearnedByDog),
  FOREIGN KEY (commandID) REFERENCES Commands(commandID),
  FOREIGN KEY (dogID) REFERENCES Dogs(dogID)
  ON DELETE CASCADE

);

-- Insert Example Data
INSERT INTO Customers (customerName, altName, phone, email)
    VALUES ('Martina Galeano','Alyssa Feutz','555-555-5555', 'martina@gmail.com'),
    ('Gail Smith', 'Brenda Smith', '555-555-5556', 'gail@gmail.com'),
    ('Alex Baker', NULL, '555-555-5557', NULL);

INSERT INTO Dogs (customerID, dogName, dogBirthday, active)
VALUES (1, 'Surco', '2022-11-10', 1),
(2, 'Josh', '2016-02-01', 1),
(2, 'Potato', '2019-05-07', 1),
(3, 'George', '2013-01-21', 0),
(3, 'Echo', '2015-08-13', 0);

INSERT INTO Employees (employeeName, employeeType)
VALUES ('Jaime Gomez', 'Trainer'),
("Rachel Li", "Office Manager"),
("Deborah Pasic", "Trainer");

INSERT INTO Commands (commandName)
VALUES ('Sit'),
('Shake'),
('Down'),
('Heal'),
('Come');

INSERT INTO TrainingSessions (customerID, dogID, employeeID, sessionDate, notes)
VALUES (1, 1, 1, "2023-02-04", "Good Boy"),
(2, 2, 1, "2023-02-04", "Good Boy"),
(2, 3, 1, "2023-02-04", "Good Boy"),
(1, 1, 3, "2023-02-05", "Ate all the treats, order more"),
(2, 2, 3, "2023-02-05", "Need to revisit down command");

INSERT INTO CommandsLearned (commandsLearnedByDog, commandID, dogID)
VALUES ("SurcoSit", 1, 1),
("SurcoDown", 3, 1),
("JoshHeal", 4, 2),
("JoshCome", 5, 2);
