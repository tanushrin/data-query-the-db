# pylint:disable=C0111,C0103

def query_orders(db):
    # return a list of orders displaying each column

    query = """SELECT * FROM Orders o ORDER BY o.OrderID ASC"""
    db.execute(query)
    results = db.fetchall()
    return results

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query = f"SELECT * FROM Orders o WHERE o.OrderDate > '{date_from}' \
        and o.OrderDate < '{date_to}' ORDER BY o.OrderDate ASC"
    db.execute(query)
    results = db.fetchall()
    return results

def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    query = "SELECT o.OrderID , o.CustomerID , o.EmployeeID , \
            o.OrderDate , o.RequiredDate , o.ShippedDate , \
            o.ShipVia , o.FreightCharge , \
            (JULIANDAY(o.ShippedDate) - JULIANDAY(o.OrderDate)) as Timedelta\
            FROM Orders o \
            ORDER BY Timedelta ASC"
    db.execute(query)
    results = db.fetchall()
    return results
