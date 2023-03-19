-- -----------------------------------------------------
-- Group 150 ~ Alyssa Feutz & Taylor Reed
-- Data Manipulation Queries
-- NOTE: Colon character being used to denote the variables that will have data from the backend programming language
-- -----------------------------------------------------


-- -----------------------------------------------------
-- (C)RUD
-- -----------------------------------------------------

-- Create Customer with no NULL data
INSERT INTO Customers (customerName, altName, phone, email)
VALUES (:customerNameInput, :altNameInput, :phoneInput, :emailInput);
-- Create Dog
-- Part I: Pre-populate dropdown box with customerName
SELECT customerID, customerName FROM Customers
-- Part II: Insert
INSERT INTO Dogs (customerID, dogName, dogBirthday, active)
VALUES (:customerIDInputFromDropdown, :dogNameInput, :dogBirthdayInput, :activeInput);
-- Create Employee
INSERT INTO Employees (employeeName, employeeType)
VALUES (:employeeNameInput, :employeeTypeInput);
-- Create Command
INSERT INTO Commands (commandName)
VALUES (:commandNameInput);
-- Create Training Session
-- Part I: Pre-populate dropdown box with customerName, dogName, employeeName
SELECT customerID, customerName FROM Customers;
SELECT dogID, dogName FROM Dogs;
SElECT employeeID, employeeName FROM Employees WHERE employeeType = "Trainer";
-- Part II: Insert
INSERT INTO TrainingSessions (customerID, dogID, employeeID, sessionDate, notes)
VALUES (:customerIDInputFromDropdown, :dogIDInputFromDropdown, :employeeIDInputFromDropdown, :sessionDateInput, :notesInput);
-- Create CommandsLearned
-- Part I: Pre-populate dropdown box with commandName and DogName
SELECT commandID, commandName FROM Commands;
SELECT dogID, dogName FROM Dogs;
-- Part II: Insert
INSERT INTO CommandsLearned (commandID, dogID)
VALUES (:commandIDinputFromDropdown, :dogIDInputFromDropdown);

-- -----------------------------------------------------
-- C(R)UD
-- -----------------------------------------------------

-- Display all customer information
SELECT * FROM Customers;
-- Display all dog information; inner join to get customer name instead of ID
SELECT dogID, Customers.customerName, dogName, dogBirthday, active FROM Dogs
INNER JOIN Customers
ON Dogs.customerID = Customers.customerID;
-- Display all employee information
SELECT * FROM Employees;
-- Display all command information
SELECT * FROM Commands;
-- Display all Training Session information; 
-- Part I inner join to get Customer/Employee names instead of IDs.
SELECT Customers.customerName, dogID, Employees.employeeName, sessionDate, notes
FROM TrainingSessions
INNER JOIN Customers
ON TrainingSessions.customerID = Customers.customerID
INNER JOIN Employees
ON TrainingSessions.employeeID = Employees.employeeID;
-- Part II to get Dog names. Not inner joined because dogID may be NULL
SELECT dogID, dogName, active FROM Dogs;
--Display all Commands Learned Information
SELECT Commands.commandName, Dogs.dogName FROM CommandsLearned
INNER JOIN Commands
ON CommandsLearned.commandID = Commands.commandID
INNER JOIN Dogs
ON CommandsLearned.dogID = Dogs.DogID;

-- -----------------------------------------------------
--CR(U)D
-- -----------------------------------------------------
-- Update entry in Customers
-- Part I: Pre-populate with current data
SELECT customerID, customerName, phone FROM Customers WHERE customerID = :customerIDInput;
SELECT altName FROM Customers WHERE customerID = :customerIDInput AND altName IS NOT NULL;
SELECT email FROM Customers WHERE customerID = :customerIDInput AND email IS NOT NULL;
-- Part II: Update
UPDATE Customers
   SET customerName = :customerNameInput, altName = :altNameInput,
       phone = :phoneInput, email = :emailInput

-- Update entry in Dogs
-- Part I: Pre-populate with current data and customer drop-down
SELECT dogID, customerID, dogName, dogBirthday, active FROM Dogs WHERE DogID = :dogIDInput;
SELECT customerID, customerName FROM Customers;
-- Part II: Update
UPDATE Dogs
   SET customerID = :customerIDInputFromDropdown, dogName = :dogNameInput, dogBirtday = :dogBirthdayInput,
       active = :activeInput
   WHERE dogID = :dogIDInput;

-- -----------------------------------------------------
--CRU(D)
-- -----------------------------------------------------
-- Delete entry in Customers
DELETE FROM Customers WHERE customerID = :customerIDInput;
-- Delete entry in Dogs
DELETE FROM Dogs WHERE dogID = :dogIDInput;
