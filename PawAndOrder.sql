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
    active bool,
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

);
