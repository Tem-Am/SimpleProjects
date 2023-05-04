import pymysql

def listProducts(maxprice):
    db = pymysql.connect(host='localhost', user='root', password='Temka2001', database='northwind')
    crsr = db.cursor()
    sql = "SELECT C.`Company`, E.`Last Name` "
    sql = sql + "FROM Customers C, Employees E, Orders O "
    sql = sql + "WHERE E.ID=O.`Employee ID` AND C.ID=O.`Customer ID` AND "
    sql = sql + "O.`Shipping Fee` < %s "
    sql = sql + "ORDER BY O.`Shipping Fee`"

    crsr.execute(sql, [maxprice])
    for row in crsr:
        print(row[0] + ": " + row[1])


if __name__ == "__main__":
    listProducts(20.5)