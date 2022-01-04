import mysql.connector
import dbconfig as cfg
class ProductDao:
    db= ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = cfg.mysql["host"],
            user = cfg.mysql["username"],
            password = cfg.mysql["password"],
            database = cfg.mysql["database"]
        )
        print ("Connection Made")

# function that allows for the creation of a product on the product table
    def create(self, product):
        cursor = self.db.cursor()
        sql = "insert into product (SerialNum, productname, manufacturer, price) values (%s,%s,%s,%s)"
        values = [
            product["SerialNum"],
            product["productname"],
            product["manufacturer"],
            product["price"]       
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid
# function that displays all from the product table
    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from product"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray= []
        print(results)
        for result in results:
            resultAsDict= self.convertToDict(result)
            returnArray.append(resultAsDict)

        return returnArray    

# function that finds a product from its serial number
    def findById(self, SerialNum):
        cursor = self.db.cursor()
        sql = "select * from product where SerialNum = %s"
        values= [ SerialNum ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
      

        return self.convertToDict(result)
        
# function that will update a product in the product table
    def update(self, product):
        cursor = self.db.cursor()
        sql = "update product set productname = %s, manufacturer = %s, price= %s where SerialNum = %s"
        values = [
            product["productname"],
            product["manufacturer"],
            product["price"],
            product["SerialNum"]       
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return product
        
# function that will delete a product from the product table
    def delete(self, SerialNum):
        cursor = self.db.cursor()
        sql = "delete from product where SerialNum = %s"
        values = [SerialNum]
        cursor.execute(sql,values)
        return {}
              



# function that will convert a row to a dictionary
    def convertToDict(self, result):
        colnames= ['SerialNum', "productname", "manufacturer", "price"]
        product = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                product[colName]= value
        return product 








productDao = ProductDao()        