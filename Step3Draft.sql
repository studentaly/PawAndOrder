-- (C)RUD
-- Create Customer
INSERT INTO Customers (customerName, altName, phone, email)
VALUES (customerNameInput, altNameInput, phoneInput, emailInput);
-- Create Dog
-- Part I: Pre-populate dropdown box with customerName
SELECT customerID, customerName FROM Customers
-- Part II: Insert
INSERT INTO Dogs (customerID, dogName, dogBirthday, active)
VALUES (customerIDInputFromDropdown, dogNameInput, dogBirthdayInput, activeInput);
-- Create Employee
INSERT INTO Employees (employeeName, employeeType)
VALUES (employeeNameInput, employeeTypeInput);
-- Create Command
INSERT INTO Commands (commandName)
VALUES (commandNameInput);
-- Create Training Session
-- Part I: Pre-populate dropdown box with customerName, dogName, employeeName
SELECT customerID, customerName FROM Customers;
SELECT dogID, dogName FROM Dogs;
SElect employeeID, employeeName FROM Employees;
-- Part II: Insert
INSERT INTO TrainingSessions (customerID, dogID, employeeID, sessionDate, notes)
VALUES (customerIDInputFromDropdown, dogIDInputFromDropdown, employeeIDInputFromDropdown, sessionDateInput, notesInput);
-- Create CommandsLearned
-- Part I: Pre-populate dropdown box with commandName and DogName
SELECT commandID, commandName FROM Commands;
SELECT dogID, dogName FROM Dogs;
-- Part II: Insert
INSERT INTO CommandsLearned (commandID, dogID)
VALUES (commandIDinputFromDropdown, dogIDInputFromDropdown);

-- C(R)UD
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
-- Display all Training Session information; inner join to get names instead of IDs
SELECT Customers.customerName, Dogs.dogName, Employees.employeeName, sessionDate, notes
FROM TrainingSessions
INNER JOIN Customers
ON TrainingSessions.customerID = Customers.customerID
INNER JOIN Dogs
ON TrainingSessions.dogID = Dogs.dogID
INNER JOIN Employees
ON TrainingSessions.employeeID = Employees.employeeID;
--Display all Commands Learned Information
SELECT Commands.commandName, Dogs.dogName FROM CommandsLearned
INNER JOIN Commands
ON CommandsLearned.commandID = Commands.commandID
INNER JOIN Dogs
ON CommandsLearned.dogID = Dogs.DogID;

--CR(U)D
-- Part I: Pre-populate drop-down box with customer names
SELECT customerID, customerName FROM Customers
-- Part II: Update
UPDATE Dogs
   SET customerID = customerIDInputFromDropdown, dogName = dogNameInput, dogBirtday= dogBirthdayInput,
       active = activeInpput
   WHERE dogID= dogIDInput

--CRU(D)
-- Delete Dog
DELETE FROM Dogs WHERE dogID= dogIDInput
-- M:M relationship deletion
DELETE FROM CommandsLearned WHERE commandID = commandIDFromInput
AND dogID = dogIDFromInput
