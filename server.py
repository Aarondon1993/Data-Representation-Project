from flask import Flask, request, redirect, abort, jsonify
from ProductDao import productDao
app= Flask(__name__, static_url_path= '', static_folder= 'staticpages')

@app.route('/', methods = ["GET", "POST"])
def index ():
    return "hello"
#get all

@app.route('/product')
def getAll():
    return jsonify(productDao.getAll())
# find By id

@app.route('/product/<int:SerialNum>')
def findById(SerialNum):
    return jsonify(productDao.findById(SerialNum)) 

@app.route('/product', methods= ['POST'])
def create():

    if not request.json:
        abort(400)     

    product = {
        "SerialNum": request.json["SerialNum"],
        "productname": request.json["productname"],
        "manufacturer": request.json["manufacturer"],
        "price": request.json["price"]
    }      
    return jsonify(productDao.create(product))

@app.route('/product/<int:SerialNum>', methods= ["PUT"])
def update(SerialNum):
    foundproduct= productDao.findById(SerialNum)
    print (foundproduct)
    if foundproduct == {}:
        return jsonify({}), 404
    currentproduct = foundproduct
    if "productname" in request.json:
        currentproduct["productname"]= request.json["productname"]
    if "manufacturer" in request.json:
        currentproduct["manufacturer"]= request.json["manufacturer"]   
    if "price" in request.json:
        currentproduct["price"]= request.json["price"] 
    productDao.update(currentproduct)                  

    return jsonify(currentproduct)


@app.route('/product/<int:SerialNum>', methods = ["DELETE"])
def delete(SerialNum):
    productDao.delete(SerialNum)
    return jsonify({"done":True})       



if __name__ == "__main__":
    app.run(debug=True)
        