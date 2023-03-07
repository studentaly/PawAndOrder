from flask import Flask, render_template, url_for, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()
app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_feutza'
app.config['MYSQL_PASSWORD'] = '3950' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_feutza'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"
mysql = MySQL(app)


# Routes

@app.route('/')
def index():
    return render_template("home.j2")

@app.route('/customers', methods=["POST", "GET"])
def customers():
    if request.method == "GET":
        query = "SELECT* FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data= cur.fetchall()

        return render_template("customers.j2", data=data)

    if request.method == "POST":
        # When user adds customer
        if request.form.get("Add Customer"):
            # user form inputs
            customerName = request.form["customerName"]
            altName = request.form["altName"]
            phone = request.form["phone"]
            email = request.form["email"]

            # account for null email AND altName
            if email == "" and altName == "":
                # mySQL query to insert a new customer into Customers
                query = "INSERT INTO Customers (customerName, phone) VALUES (%s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, phone))
                mysql.connection.commit()

            # account for null email
            elif email == "":
                query = "INSERT INTO Customers (customerName, altName, phone) VALUES (%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, altName, phone))
                mysql.connection.commit()

            # account for null altName
            elif altName == "":
                query = "INSERT INTO Customers (customerName, phone, email) VALUES (%s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, phone, email))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "INSERT INTO Customers (customerName, altName, phone, email) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, altName, phone, email))
                mysql.connection.commit()

            # redirect back to customers
            return redirect("/customers")


@app.route('/deleteCustomer/<int:customerID>')
def deleteCustomer(customerID):
    query = "DELETE FROM Customers WHERE customerID = '%s';"
    cur = mysql.connection.cursor()
    cur.execute(query, (customerID,))
    mysql.connection.commit()

    return redirect("/customers")

@app.route("/editCustomer/<int:customerID>", methods=["POST", "GET"])
def editCustomer(customerID):
    if request.method == "GET":
        query = "SELECT customerID, customerName, phone FROM Customers WHERE customerID = '%s';" % (customerID)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT altName FROM Customers WHERE customerID = '%s' AND altName IS NOT NULL;" % (customerID)
        cur = mysql.connection.cursor()
        cur.execute(query2)
        data2 = cur.fetchone()

        query3 = "SELECT email FROM Customers WHERE customerID = '%s' AND email IS NOT NULL;" % (customerID)
        cur = mysql.connection.cursor()
        cur.execute(query3)
        data3 = cur.fetchone()

        return render_template("editCustomer.j2", data=data, data2=data2, data3=data3)

    if request.method == "POST":
        # When user clicks "Edit customer"
        if request.form.get("editCustomer"):
            customerID = request.form["customerID"]
            customerName = request.form["customerName"]
            altName = request.form["altName"]
            phone = request.form["phone"]
            email = request.form["email"]

        # account for null altName AND email
            if altName == "" and email == "":
                # mySQL query to update customer in Customers DB with our form inputs
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.phone = %s, Customers.altName = NULL, Customers.email = NULL WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, phone, customerID))
                mysql.connection.commit()

            # account for null altName
            elif altName == "":
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.phone = %s, Customers.altName = NULL, Customers.email = %s WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, phone, email, customerID))
                mysql.connection.commit()

            # account for null email
            elif email == "":
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.phone = %s, Customers.altName = %s, Customers.email = NULL WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, phone, altName, customerID))
                mysql.connection.commit()

            # no null inputs
            else:
                query = "UPDATE Customers SET Customers.customerName = %s, Customers.phone = %s, Customers.altName = %s, Customers.email = %s WHERE Customers.customerID = %s"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerName, phone, altName, email, customerID))
                mysql.connection.commit()

    return redirect("/customers")

@app.route('/employees', methods=["POST", "GET"])
def employees():
    if request.method == "GET":
        query = "SELECT* FROM Employees"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data= cur.fetchall()

        return render_template("employees.j2", data=data)

    if request.method == "POST":
        # When user adds employee
        if request.form.get("Add Employee"):
            # user form inputs
            employeeName = request.form["employeeName"]
            employeeType = request.form["employeeType"]

            # All inputs are required

            query = "INSERT INTO Employees (employeeName, employeeType) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (employeeName, employeeType))
            mysql.connection.commit()

            # redirect back to employees
            return redirect("/employees")

@app.route('/commands', methods=["POST", "GET"])
def commands():
    if request.method == "GET":
        query = "SELECT* FROM Commands"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data= cur.fetchall()

        return render_template("commands.j2", data=data)

    if request.method == "POST":
        # When user adds employee
        if request.form.get("Add Command"):
            # user form inputs
            commandName = request.form["commandName"]

            # All inputs are required

            query = "INSERT INTO Commands (commandName) VALUES (%s)"
            cur = mysql.connection.cursor()
            cur.execute(query, ([commandName]))
            mysql.connection.commit()

            # redirect back to commands
            return redirect("/commands")

@app.route('/commandsLearned', methods=["POST", "GET"])
def commandsLearned():
    if request.method == "GET":
        query = "SELECT* FROM CommandsLearned"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data= cur.fetchall()

        query2 = "SELECT commandID, commandName FROM Commands"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        commandData = cur.fetchall()

        query3 = "SELECT dogID, dogName FROM Dogs"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        dogData = cur.fetchall()

        return render_template("commandsLearned.j2", data=data, commandData=commandData, dogData=dogData)

    if request.method == "POST":
        # When user adds commandbydog
        if request.form.get("Add CommandByDog"):
            # user form inputs
            commandID = request.form["commandID"]
            dogID = request.form["dogID"]

            # All inputs are required

            query = "INSERT INTO CommandsLearned (commandID, dogID) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (commandID, dogID))
            mysql.connection.commit()

            # redirect back to commandslearned
            return redirect("/commandsLearned")

@app.route('/dogs', methods=["POST", "GET"])
def dogs():
    if request.method == "GET":
        query = "SELECT* FROM Dogs"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data= cur.fetchall()

        query2 = "SELECT customerID, customerName FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        customerData = cur.fetchall()

        return render_template("dogs.j2", data=data, customerData=customerData)

    if request.method == "POST":
        # When user adds dog
        if request.form.get("Add Dog"):
            # user form inputs
            customerID = request.form["customerID"]
            dogName = request.form["dogName"]
            dogBirthday = request.form["dogBirthday"]
            active = request.form["active"]

            # All inputs are required

            query = "INSERT INTO Dogs (customerID, dogName, dogBirthday, active) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (customerID, dogName, dogBirthday, active))
            mysql.connection.commit()

            # redirect back to dogs
            return redirect("/dogs")

@app.route('/trainingSessions', methods=["POST", "GET"])
def trainingSessions():
    if request.method == "GET":
        query = "SELECT customerID, dogID, employeeID, sessionDate, notes FROM TrainingSessions"
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        query2 = "SELECT customerID, customerName FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query2)
        customerData = cur.fetchall()

        query3 = "SELECT dogID, dogName FROM Dogs"
        cur = mysql.connection.cursor()
        cur.execute(query3)
        dogData = cur.fetchall()

        query4 = "SELECT employeeID, employeeName FROM Employees WHERE employeeType = 'Trainer'"
        cur = mysql.connection.cursor()
        cur.execute(query4)
        employeeData = cur.fetchall()

        return render_template("trainingSessions.j2", data = data, dogData = dogData, customerData = customerData, employeeData = employeeData)

    if request.method == "POST":
        # When user adds a training session
        if request.form.get("Add Training Session"):
            # user form inputs
            customerID = request.form["customerID"]
            dogID = request.form["dogID"]
            employeeID = request.form["employeeID"]
            sessionDate = request.form["sessionDate"]
            notes = request.form["notes"]

            # account for null dog
            if dogID == "":
                query = "INSERT INTO TrainingSessions (customerID, employeeID, sessionDate, notes) VALUES (%s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerID, employeeID, sessionDate, notes))
                mysql.connection.commit()

            else:
                query = "INSERT INTO TrainingSessions (customerID, dogID, employeeID, sessionDate, notes) VALUES (%s, %s, %s, %s, %s)"
                cur = mysql.connection.cursor()
                cur.execute(query, (customerID, dogID, employeeID, sessionDate, notes))
                mysql.connection.commit()

        # redirect back to training sessions
        return redirect("/trainingSessions")

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9114))
    app.run(host="flip1.engr.oregonstate.edu", port=port, debug=True)
