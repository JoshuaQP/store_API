from flask import Flask , abort , request
from data import data
import json

app = Flask(__name__)

#dictionary
me = {
        "name" : "joshua",
        "last": "Palmier",
        "email": "Joshua@Gmail.com",
}

#List
products = data



@app.route("/")
@app.route("/home")
def index():
    return "hello from flask"


@app.route("/about")
def about():
    return render_template("abbout.html")

@app.route("/about/name")
def name():
    return me["name"]

@app.route("/about/fullname")
def full_name():
    return me["name"] + " " + me ["last"]

@app.route("/api/catalog")
def get_catalog():
    return json.dumps(products)

    # Get a product by its id
@app.route("/api/catalog", methods=['POST'])

def save_product():
    prod = request.get_json()
    products.append(prod)
    return json.dumps(prod)

@app.route("/api/catalog/id/<id>")
def get_product_by_id(id):
    for prod in products:
        if(prod["_id"].lower() == id):
            return json.dumps(prod)

    abort(404)


# get the cheapes product
# /api/catalog/cheapest

@app.route("/api/catalog/cheapest")
def get_cheapest():
    for prod in product:
        if(prod["prince"]  < cheapest["price"]):
            cheapest = prod

    return json.dumps(cheapest)




@app.route("/api/catalog/<category>")
def get_product_by_category(category):
    result = []
    for prod in products:
        if(prod["category"].lower() == category.lower()):
            results.append(prod)
    return json.dumps(results)


#find thr productsds witj sunch category



@app.route("/api/categories")
def get_categories():
    unique_categories =[]
    for prod in products:
        cat =prod["category"]
        if cat not in unique_Categories:
            unique_Categories.append(cat)



    return json.dumps(unique_categories) 



@app.route("/api/test")
def test():

    #add
    products.append("strawberry")
    products.append("dragon fruit")
    

    #length
    print(f"you have:{len(products)} products in your catalog")

    # iterate
    # products.remove("apple")

    for f in products:
        print(f)
      

    #   for i in range  (0,  9,1):
    #       print(i)


        #print the name 10 time

  



    return "Check your terminal"


if __name__ == '__main__':
    app.run(debug=True)