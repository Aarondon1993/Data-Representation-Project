from ProductDao import productDao

product1= {
    "SerialNum": 126,
    "productname": "Washing Machine",
    "manufacturer": "Whirlpool",
    "price": 420,
}

product2= {
    "SerialNum": 124,
    "productname": "Microwave",
    "manufacturer": "Samsung",
    "price": 250,
}

print ("create")
returnvalue = productDao.create(product1)
print(returnvalue)

print("Get all")
returnvalue = productDao.getAll()
print(returnvalue)
print("update")
returnvalue = productDao.update(product2)
print(returnvalue)
print("Get all")
returnvalue = productDao.getAll()
print(returnvalue)
print("find by id")
returnvalue = productDao.findById(product2["SerialNum"])
print(returnvalue)
print ("delete")
returnvalue = productDao.delete(product2["SerialNum"])
print(returnvalue)
print("Get all")
returnvalue = productDao.getAll()
print(returnvalue)