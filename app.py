#Code taking from https://youtu.be/2Zz97NVbH0U

from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for
)
from ProductDao import productDao
class User:
    def __init__(self, id, username, password):
        self.id= id
        self.username = username
        self.password = password

    def __repr__(self):
        return f"<User:{self.username}>"    
# Below is the two users that can login
users = []
users.append(User(id=1, username= "Aaron", password= "password"))
users.append(User(id=1, username= "gmit", password= "gmit"))
print(users)





app= Flask(__name__, static_url_path= '', static_folder= 'staticpages', template_folder='staticpages')
app.secret_key= "secretkey"

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        session.pop("user_id", None)

        username= request.form["username"]
        password= request.form["password"]

        user= [x for x in users if x.username == username][0]
        if user and user.password == password:
            session["user_id"]= user.id
            return redirect(url_for("index"))
        return redirect(url_for("login"))   

    return render_template("login.html")

@app.route("/index")
def index():
    return render_template("index.html")

#get all

@app.route('/product')
def getAll():
    return jsonify(productDao.getAll())

#find by id
@app.route('/product/<int:SerialNum>')
def findById(SerialNum):
    return jsonify(productDao.findById(SerialNum)) 
#create
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
#update
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
#delete
@app.route('/product/<int:SerialNum>', methods = ["DELETE"])
def delete(SerialNum):
    productDao.delete(SerialNum)
    return jsonify({"done":True})                  

if __name__ == "__main__":
    app.run(debug=True)
       