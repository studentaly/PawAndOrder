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
    return render_template("index.html")

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
        query = "SELECT * FROM Customers WHERE customerID = '%s';" % (customerID)
        cur = mysql.connection.cursor()
        cur.execute(query)
        data = cur.fetchall()

        return render_template("editCustomer.j2", data=data)

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
            elif altName == "":
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

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9114))
    app.run(host="flip1.engr.oregonstate.edu", port=port, debug=False)
