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


    def findById(self, SerialNum):
        cursor = self.db.cursor()
        sql = "select * from product where SerialNum = %s"
        values= [ SerialNum ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
      

        return self.convertToDict(result)
        

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
        

    def delete(self, SerialNum):
        cursor = self.db.cursor()
        sql = "delete from product where SerialNum = %s"
        values = [SerialNum]
        cursor.execute(sql,values)
        return {}
              




    def convertToDict(self, result):
        colnames= ['SerialNum', "productname", "manufacturer", "price"]
        product = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                product[colName]= value
        return product 








productDao = ProductDao()        